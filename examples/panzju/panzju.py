from EasyLogin import EasyLogin
from urllib.parse import unquote
import re
from os.path import getsize
from urllib.parse import quote

a=EasyLogin.load("panzju.status")
BLOCKSIZE=1024*1024
BLOCKHINT="MB"

DOMAIN = "https://pan.zju.edu.cn"

def login(username,password):
    """
    使用统一通行证登录新版浙大云盘pan.zju.edu.cn
    """
    global a
    x=a.get("https://pan.zju.edu.cn/sso/login",o=True)
    login_page=x.headers["Location"]
    login_service=unquote(login_page.split("service=")[1])
    x=a.post_dict("https://pan.zju.edu.cn/zjuLogin/SessionClient/login",{"username":username,"password":password,"service":login_service})
    login_status=x.json()
    if login_status["status"]!="success":
        return False
    login_service = login_status["service"]
    x=a.get(login_service,o=True)
    if x.headers["Location"]=="https://pan.zju.edu.cn/apps/files/home":
        return True
    else:
        return False

def islogin():
    """
    是否已经登录,如果已经登录返回token，否则False
    """
    global a
    x=a.get(DOMAIN+"/apps/files/home",o=True)
    t=a.b.find("input",{"id":"oc_requesttoken"})
    if t is None:
        return False
    else:
        return t["value"]


def upload(token,filename,data,filesize=None):
    """
    上传文件，与亿方云基本一致，但需要引入dont_change_cookie
    token:islogin()返回的token
    filename: 存储的文件名
    data:文件二进制数据

    返回服务器端的文件id
    """
    global a
    filename=quote(filename)
    if filesize is None:
        filesize = len(data)
    x=a.post(DOMAIN+"/apps/files/presign_upload",
             """{"folder_id":0,"file_size":%d}"""%filesize,
             headers={"requesttoken": token, "X-Requested-With": "XMLHttpRequest"})
    result=x.json()
    if result["success"]!=True:
        return False
    upload_url=result["upload_url"]
    x=a.post(upload_url,
             data,
             headers={"requesttoken": token,"X-File-Name":filename},dont_change_cookie=True)
    result=x.json()
    if result["success"]!=True:
        return False
    return result["new_file"]["typed_id"]

def share(token,fileid):
    """
    分享一个文件，fileid来自upload，返回文件分享链接file_unique_name
    可以反复执行，返回相同的分享链接
    """
    global a
    x=a.post(DOMAIN+"/apps/files/share",
             """{"access": "public", "disable_download": "0", "due_time": "never_expire", "password_protected": false,"item_typed_id": "%s"}"""%fileid,
             headers={"requesttoken":token,"X-Requested-With": "XMLHttpRequest"})
    result=x.json()
    if result.get("success")!=True:
        return False
    else:
        return result["share_link"]["unique_name"]

finder=re.compile(r'''file_(\d+)''')

def download(file_uniqe_name):
    """
    获得一个分享链接的直接链接
    本函数可能被频繁调用，为优化性能不使用BeautifulSoup
    :param file_uniqe_name: 分享链接，来自share
    :return: 可以直接下载的url，一段时间后失效
    """
    a=EasyLogin()
    page=a.get(DOMAIN+"/share/"+file_uniqe_name,result=False)
    fileid = finder.search(page).group(1)
    x=a.get(DOMAIN+"/apps/files/download?file_id={}&scenario=share".format(fileid),o=True)
    return x.headers["Location"]

def block(fp):
    """
    使用分块上传解决大文件传输的内存问题
    每次产生一个BLOCKSIZE的数据进行传输，传输好后再读取下一个BLOCK
    :param fp: 文件读入，传入open(filename,"rb")
    :return: 用yield产生的generator，可以被EasyLogin(requests)正常处理
    """
    x = fp.read(BLOCKSIZE)
    i = 1
    while len(x):
        print("{}{}".format(i,BLOCKHINT))
        i+=1
        yield x
        del x
        x = fp.read(BLOCKSIZE)

if __name__=="__main__":
    import sys
    token = islogin()
    if not token:
        print("Login!")
        login(sys.argv[2],sys.argv[3])
        a.save("panzju.status")
        token=islogin()
    block_generator=block(open(sys.argv[1],"rb"))
    filesize=getsize(sys.argv[1])
    fileid=upload(token,sys.argv[1],block_generator,filesize)
    file_uniqe_name=share(token,fileid)
    print("fileid:")
    print(fileid)
    print()
    print("Share Link:")
    print(DOMAIN+"/share/"+file_uniqe_name)
    print()
    print("Download Link (expire soon):")
    print(download(file_uniqe_name))
