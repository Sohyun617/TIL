import scrapy
from myscraper.items  import MyscraperItem

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = ['http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dd/dt[2]/a/text()').extract()
        author = response.css('.writing::text').extract()
        preview = response.css('.lede::text').extract()

        item =[]
        for idx in range(len(titles)):
            item = MyscraperItem()
            item['title']= titles[idx]
            item['author']= authors[idx]
            item['preview']= previews[idx]
            items.append(item)


        pass
