import scrapy
from scrapy.linkextractors import LinkExtractor
class PostsSpider(scrapy.Spider):
    name = "posts"
    allowed_domains = ["www.s2wlab.com"]
    start_urls = [
        "https://www.s2wlab.com/index.html"
    ]

    def parse(self, response):
        extractor = LinkExtractor(allow_domains='s2wlab.com')
        links = extractor.extract_links(response)
        for link in links:
            self.start_urls.append(link.url)
        print(self.start_urls)
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
