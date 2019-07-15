# -*- coding: utf-8 -*-

# @File    : utils.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu


import hashlib

import re
import requests
from datetime import datetime, timedelta


def get_md5(content):
    return hashlib.md5(content.encode()).hexdigest()


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return response


def parse_time(time_str):
    now = datetime.now()
    minute_result = re.search("(\d+) 分钟前", time_str)
    hour_result = re.search("(\d+) 小时前", time_str)
    day_result = re.search("(\d+) 天前", time_str)

    if minute_result:
        minutes = minute_result.group(1)
        dt = now - timedelta(minutes=int(minutes))

    elif hour_result:
        hours = hour_result.group(1)
        dt = now - timedelta(hours=int(hours))

    elif day_result:
        days = day_result.group(1)
        dt = now - timedelta(days=int(days))
    else:
        dt = now

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def paginate(page, paginate_by=20):
    if page > 0:
        page -= 1
    elif page < 0:
        page = 1

    return {
        "limit": paginate_by,
        "offset": page * paginate_by
    }