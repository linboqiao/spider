# epubee����������

�����Ӷ�cn.epubee.com�ϵĵ��������ص�ַ������٣�ʹ��mpms����̶��߳�ִ����������

## ����׼������

[����Python�����-���߳�������� mpms](https://github.com/aploium/mpms)

## ����˵��

���������Ҫ�ο�mpms���������ӣ���������ӻ����Ͷ����������ļ��Ŀ�ܣ�mpms����Ʋ��ڴ˴������۷�Χ

```
worker������
    ���溯����ʹ��EasyLogin�������ȡ����
    ����ҳ��id����������һ�������list

handler������
    ����һ��meta����Ҫ����worker�����з���ֵ
    ���е��߳�ͬʱֻ����һ��handler��ִ�У�����ֻӦ�����д�ļ��Ⱥ�ʱ���ٵĲ���

main������
    ���ļ����������У���ѭ��������������У�join�ȴ����
```

## ���дд

���߳����������Ч�ʣ�mpms������ͦ�򵥵ģ�ֻҪ��ģ��ͺ���23333

ע��print����Ҳ��һ���ǳ���ʱ�Ĳ�����Ӧ�þ�����print

����������������������ӣ������������Ҫ��һ���Ĵ�����downloadlink.txt��������ǰ׺����wget --content-disposition -nc -i downloadlink.txt

ÿдһ�����Ӿͷ���EasyLogin������Ҫ�Ľ��ĵط�����ζ�EasyLogin��init����������session��������ֹÿ��worker������Session������˷�ʱ��

���������EasyLogin�����ǲ��ܹ���ģ������ڸ߲�����ʱ����ܶ���߳�ͬʱ�޸�a.b��֮���a.getlist����Ϲ����Orz �����˶������ѡ���ڽ��̼�����Session����ע��worker�������ò���ȫ�������̹߳���ı����ģ�

���������Ķ�EasyLogin��֧�ָ߲�����û��Ч���������Կ�

ʹ��wget�����ƺ��������������⣬һ��������������ļ����ͺ���ɾ����������pythonһ��������curl -OJ��

## Example Code for further download

```
c=input()
while True:
    print("http://cn.epubee.com/"+c)
    try:
        c=input()
    except:
        break
```

```
from os import system
for line in open("filelist.txt"):
    url=line.replace("\n","")
    print(url)
    system("curl -OJ \"{}\"".format(url))
```
