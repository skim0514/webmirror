import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import os
class TestSpider(scrapy.Spider):
    name = "test"
    # allowed_domains = ["www.s2wlab.com"]
    start_urls = [
        "https://stackoverflow.com/questions/6499603/python-scrapy-convert-relative-paths-to-absolute-paths"
    ]

    def parse(self, response):
        page = 'post.html'
        with open(page, 'wb') as f:
            f.write(response.body)
        
   