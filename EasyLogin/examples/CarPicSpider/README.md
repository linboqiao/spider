# CarPicSpider

��ȡ����֮�ҵ���������ͼƬ

Inspired by https://github.com/FindHao/CarPicSpider

![screenshot](screenshot.jpg)

[pic_result.rar](https://api.chenyuan.me/fangcloud2/210001485088) 427.63MB��**����ǰ����Star����Ŀ**

## ֱ������

ֱ�����н����������ļ���`record.txt`��`download_command.bat`

    record.txt�ĸ�ʽΪ��Ʒ����\t��������\tͼƬurl

    download_command.bat������curl.exeִ����������

`result.zip`�ṩ�������ļ���**����ǰ����Star����Ŀ**��[��������](https://raw.githubusercontent.com/zjuchenyuan/EasyLogin/master/examples/CarPicSpider/result.zip)

## Cache����

��exampleʹ����`Cache=True`��������ʾ��`md5(url)`��Ϊ`�����ļ����ļ���`

�ṩ`cache_files.zip`����ѹ����Ŀ¼�󼴿ɲ������κ��������󣬴Ӷ�ʵ�ֿ���ѭ����[��������](https://raw.githubusercontent.com/zjuchenyuan/EasyLogin/master/examples/CarPicSpider/cache_files.zip)

## ����˵��

### gethot

    ������֮�ҹ����ֻ���������Ʒ��

    ����һ��dict��{ Ʒ������:[����url��Ʒ��ƴ��]}

### getbrand(url):

    ����һ��Ʒ�Ƶ�url����url���Դ�gethot�������

    �������飬��Ԫ��Ϊ��[���ƣ��۸����ͣ�ͼƬurl������url��id]

    ����ͼƬurl�����滻�������Ϊ640x480����֪����壩��ͼƬurl

### morepic(id):

    ��һ�����͵õ�����ĳ���ͼƬ��id����getbrand���������

    ����ͼƬurl������

    ����url�����滻�������Ϊ640x480����֪����壩��ͼƬurl

