## �ڷ���API

ʹ��EasyLogin��ɡ��ڷ��ơ���¼���ϴ�����������ֱ����ȡ

### ʹ�÷���

����EasyLogin��ʹ��ʾ�������ȷ���https://github.com/zjuchenyuan/EasyLogin

���غ�EasyLogin.py�������������װ

    python3 run.py ���ϴ����ļ��� �ڷ����û��� �ڷ�������

![screenshot](screenshot.png)

### ˵��

����ע���ڷ��� https://www.fangcloud.com/auth/register �������20G�洢

��������Զ����桢�����¼״̬��fangcloud.status��ʹ��EasyLogin�ṩ��**save**��**load**������

������cookieû��ʧЧʱ�����ᷢ���¼������ͼ��ʾ����ʱ���Բ��ṩ�û����������

#### ����˵��

```
login(username,password) #�û��������¼�ڷ���
islogin() #�Ƿ��Ѿ���¼,����Ѿ���¼����token������False
upload(token,filename,data) #�ϴ��ļ�������fileid
share(token,fileid) #�����ļ������ط����ַfile_unique_name
download(file_uniqe_name) #���ļ������ַ�õ�ֱ����������URL����������Ҫ���¼��Ҳ����ʹ�õ�¼״̬
```