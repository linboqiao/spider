# EasyLogin.py

对requests和BeautifulSoup进一步封装，写爬虫代码更轻松~

## Requirements 请先安装依赖，仅支持Python3

    pip3 install -U requests[socks] bs4 -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com
    
## Note 说明

Useful thing is only `EasyLogin.py`. All directories are examples, not needed for running.

只需要下载EasyLogin.py就够了，examples文件夹是使用EasyLogin开发的例子们

## Quickstart 来试试看吧~

Using EasyLogin is very EASY!

First, import it and create an object:  首先导入包并创建一个对象

    from EasyLogin import EasyLogin
    a = EasyLogin()
    
Then, make a get request or post request: 发起一个请求

    a.get("http://ip.cn")

Finally, I need the `code` tag: 我需要的东西在`<code>`标签里面，我们把它拿出来

    IP,location = a.f("code",attrs={})
    print(IP)
    print(location)

Moreover, I also need img, css, js and text: 我还需要网页中出现的图片、CSS、JS的链接以及文本

    print(a.img())
    print(a.css())
    print(a.js())
    print(";".join(a.text()))

## Documentation 文档

待完成...
    
简单地说，用get或post后self.b就是BeautifulSoup的对象

## 开发方法

> 论爬虫是怎么简单地被写出来的

1. 先完成一遍手动的不带工具流程，观察把握整体感觉

2. 打开Chrome开发者工具或者Burp，查看关键性的请求包

3. 写点初始化的代码，引入包，a=EasyLogin()

4. 分析请求内容，从网页源代码或者其他请求中找到蛛丝马迹，拼凑出正确的请求包

    这一步就也许需要先get，从源代码得到token的操作和得到cookie
    
    （EasyLogin会自己处理好cookie，无需费心）

5. 发出post请求，分析返回的内容

    或许是个json？可以x.json()
    
    一般可能就是个页面，那就a.b.find吧
    
    （a是EasyLogin的对象，a.b是BeautifulSoup的对象，戳→[这里](http://cuiqingcai.com/1319.html)←看看BeautifulSoup怎么用）

6. 服务器能正确响应就基本完事啦，不妨再提取成函数、封装成类、给我发起一个Pull请求？