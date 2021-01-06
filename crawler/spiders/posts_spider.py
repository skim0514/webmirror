import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import os
# import tinycss
class PostsSpider(scrapy.Spider):
    name = "posts"
    allowed_domains = ["www.s2wlab.com"]
    start_urls = [
        "https://www.s2wlab.com/index.html"
    ]
    count = len(start_urls)

    def parse(self, response):
        extractor = LinkExtractor()
        links = extractor.extract_links(response)
        for link in links:
            print(link)
            yield Request(link.url, callback=self.parse_page)  
 
    def parse_page(self, response):
        for script in response.xpath('//script/@src').getall():
            # print(script)
            yield Request(response.urljoin(script), callback=self.parse_script)
        for image in response.xpath('//image/@src'):
            print(image)
            yield Request(response.urljoin(image), callback=self.parse_script)
        for link in response.xpath("//link[@rel='stylesheet']/@href").getall():
            yield Request(response.urljoin(link), callback=self.parse_script)

        page = response.url.split('/')[-1]
        if page.split('.')[-1] != 'html':
            page = 'home.html'
        #filename = 'posts' + str(self.count) + '.html'
        self.count += 1
        with open(page, 'wb') as f:
            f.write(response.body)


    def parse_script(self, response):
        folder = response.url.split('/')[-2]
        page = './' + folder + '/' + response.url.split('/')[-1]
    
        try:
            with open(page, 'wb') as f:
                f.write(response.body)
        except:
            os.mkdir(folder)
            with open(page, 'wb') as f:
                f.write(response.body)

            

        
        
        # count = 0
        # for link in links:
        #     filename = 'posts' + str(count) + '.html'
        #     with open(filename, 'wb') as f:
        #         f.write(link.body)
        #     count += 1
        #     f.close()
        # items = []
        # for link in set(response.xpath('//a/@href').extract()):
        #     item = Links()
        #     if len(link) > 1:
        #         if link.startswith("/") or link.startswith("."):
        #             url = response.urljoin(link)
        #             item['internal'] = url
        #         elif link.startswith("http") or link.startswith()
        # page = response.url
        # filename = 'posts.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
