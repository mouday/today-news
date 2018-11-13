# -*- coding: utf-8 -*-

# @File    : weixin_spider.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu

"""
微信文章抓取
通过搜狗微信分类首页
http://weixin.sogou.com/
"""

from datetime import datetime

import requests
import urllib3
from scrapy import Selector

from models import ArticleModelUtils
from .image_download import download

urllib3.disable_warnings()


def crawl_weixin(url, tag):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    sel = Selector(response)
    lis = sel.css(".news-list li")
    for li in lis:
        image_url = li.css(".img-box img::attr(src)").extract_first()
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        image = download(image_url)
        title = li.css("h3 a::text").extract_first()
        article_url = li.css("h3 a::attr(href)").extract_first()
        summary = li.css(".txt-info::text").extract_first()
        source = li.css(".s-p a::text").extract_first()
        source_url = li.css(".s-p a::attr(href)").extract_first()
        publish_time = li.css(".s-p::attr(t)").extract_first()
        publish_time = datetime.fromtimestamp(int(publish_time)).strftime("%Y-%m-%d %H:%M:%S")

        item = {
            "title": title,
            "article_url": article_url,
            "source": source,
            "source_url": source_url,
            "summary": summary,
            "tag": tag,
            "publish_time": publish_time,
            "image": image,
        }

        yield item


def crawl():
    links = [
        {
            "url": "https://weixin.sogou.com/pcindex/pc/pc_5/pc_5.html",
            "tag": "科技"},
        {
            "url": "https://weixin.sogou.com/pcindex/pc/pc_6/pc_6.html",
            "tag": "财经"
        }
    ]
    count = 0
    for link in links:
        for item in crawl_weixin(link["url"], link["tag"]):
            ret = ArticleModelUtils.insert(item)
            if ret is True:
                count += 1

    return count


if __name__ == '__main__':
    crawl()
