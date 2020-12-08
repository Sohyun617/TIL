import scrapy
from mymovie.items import MymovieItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = ['http://movie.naver.com/movie/point/af/list.nhn']

    def parse(self, response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        ratings = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        authors = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/a/text()').extract()
        cdates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
        items=[]
        for idx in range(len(titles)):
            item = MymovieItem()
            item['title']= titles[idx]
            item['rating']= ratings[idx]
            item['author']= authors[idx]
            item['cdate']=cdates[idx]
            items.append(item)
        
        return items
