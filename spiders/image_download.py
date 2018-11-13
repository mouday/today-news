# -*- coding: utf-8 -*-

# @File    : image_download.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu
import os

import requests
import urllib3

from .utils import get_md5

urllib3.disable_warnings()
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = "static/images"
IMAGE_PATH = os.path.join(BASE, IMAGE_DIR)

def download(image_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    response = requests.get(image_url, headers=headers)

    if not os.path.isdir(IMAGE_PATH):
        os.makedirs(IMAGE_PATH)

    filename = "{}.jpg".format(get_md5(response.text))
    file_path = os.path.join(IMAGE_PATH, filename)

    with open(file_path, "wb") as f:
        f.write(response.content)

    return os.path.join(IMAGE_DIR, filename)


if __name__ == '__main__':
    url = "https://img03.sogoucdn.com/net/a/04/link?appid=100520033&url=http%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2Fdkz9bibRJqAqCXOXKlBb827pFWdsc4d0xjrT9g0c6MXZ6Z6noWKPjYZj0wcgo2juwlPfZb3py8XszDPYwfIqegg%2F0%3Fwx_fmt%3Djpeg"
    print(download(url))
