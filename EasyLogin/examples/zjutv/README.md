#�㽭��ѧ�㲥��������Ƶ����

## ������Դ

�磺2013��ͨ��������ͦ����˼�ģ��������

https://www.zdgd.zju.edu.cn/index.php?s=/home/player/index/id/7.html

## �������Ҫ���ݿ�

�������ݿ⡢����
```sql
CREATE DATABASE zjutv DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `description` longtext CHARACTER SET utf8,
  `mp4` varchar(555) CHARACTER SET utf8 DEFAULT NULL,
  `share` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## ����˵�� run.py

����������ƵidΪ750�����Ǵ�1~751����ѭ�����������ݿ���: id(����URL)����Ƶ���⣬��Ƶ���(����\n)��mp4��������

ʵ�����з���ĳЩid��û�ж�Ӧ��Ƶ��������Ƶ�����ڣ�ʹ����try-except��������

## �������ݿ�෽��

    SELECT mp4 FROM `data` where mp4 like 'http%' and mp4 like '%cernet%';

ִ���Ͼ�sql��ȡ��������Ч���������ӣ���wget�������أ�

    wget -i list.txt  --referer="https://www.zdgd.zju.edu.cn/index.php?s=/home/player/index/id/550.html" -c

������֪ʶ��~��ô��wget֮**����Referer�ƿ�������**��**�б���������**��**�ϵ�����**

Ȼ�����Ƕ��ļ��ĸ����֣�

    SELECT "move",SUBSTRING_INDEX(mp4, '/', -1),id,".mp4" FROM `data` where mp4 like 'http%' and mp4 like '%cernet%';
    
��ִ�н�����Ƶ�bat�У����޸�һ��\t����ִ�п�

## ��������Ž�ͼ

��һ�θ��ܵ����ҵ�ǧ�����٣�

![screenshot1.jpg](screenshot1.jpg)

����36.7G���ʵ�Ǻܶ���Ƶ�������ԣ����ز��ˣ���

![screenshot2.jpg](screenshot2.jpg)

������Ƶʱ���Ÿ��򿴿�������ǿ�ѧ���񣩣�

![screenshot3.jpg](screenshot3.jpg)