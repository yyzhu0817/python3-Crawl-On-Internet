# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # collection = table = 'images' # 代表mongodb 和 mysql 存储的名称
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    thumb = scrapy.Field()
