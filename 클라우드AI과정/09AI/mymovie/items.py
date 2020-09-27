# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MymovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title= scrapy.Field()
    rating = scrapy.Field()
    author = scrapy.Field()
    cdate = scrapy.Field()
    pass
