
# toutiao项目说明

仿照今日头条，做一个自己的头条

![](images/toutiao.png)


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