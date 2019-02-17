# -*- coding: utf-8 -*-
import scrapy

class GuchengSpider(scrapy.Spider):
    name = 'gucheng'
    # allowed_domains = ['hq.gucheng.com'] 无用删除
    start_urls = ['https://hq.gucheng.com/gpdmylb.html'] # 爬虫起始地址

    def parse(self, response):
        # XPath选择器
        #   stocks = response.xpath('//*[@id="stock_index_right"]/div[3]/section/a/text()')
        # CSS选择器
        stocks = response.css('#stock_index_right > div.stock_sub > section > a::text')
        for val in stocks:
            print(val.get())
