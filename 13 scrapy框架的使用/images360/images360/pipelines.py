# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from . import settings


# class Images360Pipeline(object):
#     def process_item(self, item, spider):
#         return item


class Images360MongoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT

        conn = pymongo.MongoClient(host=host, port=port)
        self.db = conn.搜图片
        self.myset = self.db.图片

    def process_item(self, item, spider):
        # item转化为字典
        self.myset.insert(dict(item))
        print('存入数据库成功')
        return item

    # def close_spider(self, spider):
    #     self.db.close()


class Images360MysqlPipeline():
    def __init__(self):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        pwd = settings.MYSQL_PWD
        dbName = settings.MYSQL_DB
        self.db = pymysql.connect(host=host, user=user, password=pwd, database=dbName, charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        insert = 'insert into images values (%s,%s,%s,%s);'
        L = [item["id"],
             item["url"],
             item["title"],
             item["thumb"]
             ]
        self.cursor.execute(insert, L)
        self.db.commit()

    def close_spider(self, spider):
        self.db.close()


class ImagePipeline(ImagesPipeline):
    '''
    内置的 Images Pipeline 会默认读取 Item 的 image_urls 字段， 并认为该字段是一个列表形式，
    会遍历 Item 的 image_urls 字段， 然后取出每个 URL 进行图片下载。
    但是现在生成的 Item 的图片链接字段并不是 image_urls 字段表示的，也不是列表形式，
    而是单个的URL。所以为了实现下载，我们需要重新定义下载的部分逻辑，即要自定义ImagePipeline，继承内置的Images Pipeline，重写几个方法
    '''

    # def file_path(self, request, response=None, info=None):
    #     url = request.url
    #     file_name = url.split('/')[-1]
    #     return file_name

    def item_completed(self, results, item, info):
        # 是当单个 Item 完成下载时的处理方法
        # 第一个参数results就是该Item对应的下载结果,它是一个列表形式,列表每一个元素是一个元组
        # results = [(True, {'url': 'https://p5.ssl.qhimgs1.com/t0172fcb9ecb09c6b85.jpg', 'path': 't0172fcb9ecb09c6b85.jpg', 'checksum': 'c80e23a8296b056da12ab9c001ae5867'})]
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('图片下载失败，抛出DropItem异常')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])
