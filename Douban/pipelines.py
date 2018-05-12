# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
# from Douban import settings
from scrapy.conf import settings


class DoubanPipeline(object):

    def open_spider(self,spider):

        host = settings['MONGO_HOST']
        post = settings['MONGO_POST']
        dataname = settings['MONGO_DB']
        movie_col = settings['MONGO_COL']

        self.client = MongoClient(host, int(post))
        # self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client[dataname]
        self.col = self.db[movie_col]


    def process_item(self, item, spider):

        dict_data = dict(item)
        print(11111111111111111111,dict_data)
        self.col.insert(dict_data)

        return item

    def close_spider(self,spider):
        self.client.close()