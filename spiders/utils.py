# -*- coding: utf-8 -*-

# @File    : utils.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu


import hashlib


def get_md5(content):
    return hashlib.md5(content.encode()).hexdigest()
