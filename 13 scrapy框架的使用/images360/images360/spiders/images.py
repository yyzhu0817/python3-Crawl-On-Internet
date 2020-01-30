# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy import Request

from ..items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):  # 构造Request,此Request是get请求方式
        data = {'ch': 'photography', 'listtype': 'new'}
        base_url = 'https://image.so.com/zjl?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            url = base_url + urlencode(data)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)  # 解析Json ,转为字典
        for image in result['list']:
            item = Images360Item()
            item['id'] = image['id']
            item['url'] = image['qhimg_url']
            item['title'] = image['title']
            item['thumb'] = image['qhimg_thumb']
            yield item
