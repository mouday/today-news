# -*- coding: utf-8 -*-

# @Date    : 2018-12-17
# @Author  : Peng Shiyu


import time

from flask import render_template, request, jsonify
from playhouse.shortcuts import model_to_dict

from models import ArticleModel
from spiders import toutiao_spider, weixin_spider, segmentfault_spider


def index():
    page = int(request.args.get("page", "1"))
    tag = request.args.get("tag", "")

    # 分页控制
    if page < 1:
        page = 1

    # 标签查询
    if tag:
        rows = (ArticleModel
                .filter(ArticleModel.tag == tag)
                .order_by(-ArticleModel.publish_time)
                .paginate(page))
    else:
        rows = (ArticleModel
                .select()
                .order_by(-ArticleModel.publish_time)
                .paginate(page))

    return render_template("toutiao.html", rows=rows, page=page, tag=tag)


def crawl():
    start_time = time.time()
    # toutiao_count = toutiao_spider.crawl()
    # weixin_count = weixin_spider.crawl()
    segmentfault_count = segmentfault_spider.crawl()

    time_span = int(time.time() - start_time)
    return jsonify({
        # "toutiao_count": toutiao_count,
        # "weixin_count": weixin_count,
        "segmentfault_count": segmentfault_count,
        "time_span": time_span
    })
