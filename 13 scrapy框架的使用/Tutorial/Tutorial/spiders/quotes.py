# -*- coding: utf-8 -*-
import scrapy

from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for i in quotes:
            item = TutorialItem()

            item['text'] = i.css('.text::text').get()
            item['author'] = i.css('.author::text').get()
            item['tags'] = i.css('.tag::text').getall()
            yield item

        next = response.css('.next a::attr(href)').get()  # 得到下一页的链接:'/page/2/'
        next_url = response.urljoin(next)  # urljoin()方法可以将相对 URL 构造成一个绝对的 URL
        yield scrapy.Request(url=next_url, callback=self.parse)
