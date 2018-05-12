# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_url = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 编剧
    scripter = scrapy.Field()
    octor = scrapy.Field()
    style = scrapy.Field()
    create_country = scrapy.Field()
    language = scrapy.Field()
    show_date = scrapy.Field()
    longer = scrapy.Field()
    other_name = scrapy.Field()
    desc = scrapy.Field()

    pass
