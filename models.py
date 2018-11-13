# -*- coding: utf-8 -*-

# @File    : models.py
# @Date    : 2018-09-13
# @Author  : Peng Shiyu
import logging
import os

from datetime import datetime

from spiders.utils import get_md5
from peewee import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "article.db")

db = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db


class ArticleModel(BaseModel):
    title = CharField()
    article_url = CharField()
    source = CharField()
    source_url = CharField()
    summary = CharField()
    tag = CharField()
    publish_time = DateTimeField()
    image = CharField()

    create_time = DateTimeField
    md5 = CharField(unique=True)


if not ArticleModel.table_exists():
    ArticleModel.create_table()


class ArticleModelUtils(object):
    @classmethod
    def insert(cls, item):
        content = "{}{}".format(item.get("title"), item.get("source"))
        item["md5"] = get_md5(content)
        item["create_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        is_insert = False

        try:
            ArticleModel.create(**item)
            logging.debug("ArticleModel insert successful")
            is_insert = True
        except IntegrityError as e:
            logging.debug("ArticleModel {}".format(e))

        return is_insert
