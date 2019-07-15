
# Today News

## 项目简介

通过抓取微信文章和今日头条新闻，仿照今日头条，打造一个自己的今日头条

![](images/toutiao.png)


## 基本思路

```
新闻下载 -> 新闻存储 -> 新闻展示
```

抓取源：

1. 今日头条app新闻

https://lf.snssdk.com/api/news/feed/v88/

2. 搜狗微信首页新闻

https://weixin.sogou.com/

备注

微信文章的图片地址会过期，所有抓取的时候直接保存到本地

```
static/images
```

## 项目使用模块

- 下载器使用了：requests
- 解析器使用了：scrapy.Selector
- 存储器使用了：peewee
- web框架使用了：Flask

## 启动运行
```
git clone https://github.com/mouday/today-news.git
cd today-news
pip install -r requirement.txt
python run.py

```
访问地址就可以打开：http://127.0.0.1:5000/


## 扩展
如果需要更多的新闻源，可以自己抓取新的新闻源，放在`spiders`文件夹下，按照如下字段解析

```python
item = {
    "title": title,   # 新闻标题
    "article_url": article_url,  # 新闻链接
    "source": source,   # 新闻发布者
    "source_url": source_url,  # 发布者链接
    "summary": summary,   # 新闻概要
    "tag": tag,  # 新闻标签
    "publish_time": publish_time,  # 新闻发布时间,datetime类型
    "image": image,  # 新闻图片
    }

```

将解析好的`item` 调用函数存入数据库
```python
from models import ArticleModelUtils

ArticleModelUtils.insert(item)
```

这样前台就可以显示了

当然，如果有好的新闻源，可以提交到这个仓库，6小时之内会给出答复

## 转载
本项目已推荐给微信公众号：Python那些事（微信号：PythonSomething），推送的文章内容质量还不错，在同类公众号里边属于中上等了，学习Python可以关注

## TODO
sf: https://segmentfault.com/t/python
掘金： https://juejin.im/tag/Python
知乎：https://www.zhihu.com/topic/19552832/hot
csdn： https://www.csdn.net/nav/newarticles


# Python头条

TODO:
爬虫模块
数据模块
接口模块
前端模块
app模块
