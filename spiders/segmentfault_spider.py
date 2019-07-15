# -*- coding: utf-8 -*-

# @Date    : 2018-12-17
# @Author  : Peng Shiyu


from urllib.parse import urljoin

from parsel import Selector

from models import ArticleModelUtils
from spiders.utils import parse_time, get_response


def crawl_segmentfault():
    """
    思否python专栏文章
    """
    base_url = "https://segmentfault.com"

    url = "https://segmentfault.com/t/python/blogs"
    response = get_response(url)

    sel = Selector(text=response.text)
    articles = sel.css(".stream-list .stream-list__item")
    for article in articles:
        title = article.css("h2 a::text").extract_first("")
        article_url = article.css("h2 a::attr(href)").extract_first("")

        if article_url.startswith("/"):
            article_url = urljoin(base_url, article_url)

        publish_time = article.css(".list-inline span").xpath("string(.)").extract_first("")
        publish_time = parse_time(publish_time)
        item = {
            "title": title,
            "article_url": article_url,
            "source": "思否",
            "source_url": "https://segmentfault.com/t/python",
            "summary": "",
            "tag": "Python",
            "publish_time": publish_time,
            "image": "",
        }
        yield item


def crawl():
    count = 0
    for item in crawl_segmentfault():
        ret = ArticleModelUtils.insert(item)
        if ret is True:
            count += 1

    return count


if __name__ == '__main__':
    crawl()
