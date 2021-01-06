import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import os
class TestSpider(scrapy.Spider):
    name = "test"
    # allowed_domains = ["www.s2wlab.com"]
    start_urls = [
        "https://www.s2wlab.com/contact.html"
    ]

    def parse(self, response):
        page = 'post.html'
        with open(page, 'wb') as f:
            f.write(response.body)
        
   