# scraper

数据获取模块。

本文档主要定义数据存储格式。

## weibo

文件存储在[这个文件夹](../app/scraper/store/weibo)下。

文件名为`weibo_<date>.csv`。

文件格式见实例。

## bilibili

bilibili的文件首先存储于[raw](../app/scraper/raw)文件夹下。

然后通过`operation.py`中的操作来对时间进行分类。

文件存储于[这个文件夹](../app/scraper/store/bilibili)下。

文件名为`bilibili_<date>.csv`。

文件格式见实例。

## south

文件存储在[这个文件夹](../app/scraper/store/south)下。

文件名为`south_<date>.csv`。

文件格式，以时间为分类标准，每个文件内只需要正文，例如：

```text
------
south_<date_1>.csv
---
<content_1>
<content_2>
------
south_<date_2>.csv
---
<content_3>
<content_4>
------
```

## 其它

- 原本准备爬取人民日报，但是难以解决关键词筛选的问题，故放弃；
- south的爬虫文件调用不了，望解决。
- south爬取的数据已push——潘昱光