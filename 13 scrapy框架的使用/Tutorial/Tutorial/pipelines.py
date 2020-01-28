# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymongo
from scrapy.exceptions import DropItem

from . import settings


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')


class MongoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT

        conn = pymongo.MongoClient(host=host, port=port)
        self.db = conn.教程
        self.myset = self.db.教程内容

    def process_item(self, item, spider):
        # item转化为自带呢
        self.myset.insert(dict(item))
        print('存入数据库成功')

    def close_spider(self, spider):
        self.db.close()
