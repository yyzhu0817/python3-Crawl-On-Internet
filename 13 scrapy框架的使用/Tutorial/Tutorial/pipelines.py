# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
from scrapy.exceptions import DropItem


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        # 删掉 text 中长度超过50个的item
        if item['text'] and len(item['text']) > self.limit:
            item['text'] = item['text'][:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Text 丢失')


class MongoPipeLine(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # @classmethod
    # def pass
