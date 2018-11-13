# -*- coding: utf-8 -*-

# @File    : toutiao_flask.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu


import time

from flask import Flask
from flask import render_template, request, jsonify

from models import ArticleModel
from spiders import toutiao_spider
from spiders import weixin_spider

app = Flask(__name__)


@app.route("/")
def index():
    page = int(request.args.get("page", "1"))
    if page < 1:
        page = 1

    rows = (ArticleModel
            .select()
            .order_by(-ArticleModel.publish_time)
            .paginate(page))
    return render_template("toutiao.html", rows=rows, page=page)


@app.route("/crawl")
def crawl():
    start_time = time.time()
    toutiao_count = toutiao_spider.crawl()
    weixin_count = weixin_spider.crawl()
    time_span = int(time.time() - start_time)
    return jsonify({
        "toutiao_count": toutiao_count,
        "weixin_count": weixin_count,
        "time_span": time_span
    })


if __name__ == '__main__':
    app.run(debug=True)
