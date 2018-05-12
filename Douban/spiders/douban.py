# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Douban.items import DoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'top250'),follow=True ),
        Rule(LinkExtractor(allow=r'subject'), callback='parsr_detarl'),
        # Rule(LinkExtractor(allow=r'celebrity'), callback='parsr_celebrity'),
    )

    # def parse_item(self, response):
    #     i = {}
    #     print('------------',response.url)
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #
    #
    #     return i

    def parsr_detarl(self,response):

        # print(2222222222222222222222,response.request.headers['User-Agent'])

        item = DoubanItem()
        print('+++++++++++++++',response.url)
        item['movie_name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        item['movie_url'] = response.url
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first()
        item['scripter'] = ",".join(response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract())
        item['octor'] = ",".join(response.xpath('//*[@id="info"]/span[3]/span[2]/span/a/text()').extract())

        item['style'] = ','.join(response.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract())

        item['create_country'] = response.xpath('//*[@id="info"]/text()[8]').extract_first()
        item['language'] = response.xpath('//*[@id="info"]/text()[10]').extract_first()
        item['show_date'] = ','.join(response.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract())
        item['longer'] = response.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').extract_first()
        item['other_name'] = response.xpath('//*[@id="info"]/text()[17]').extract_first()
        item['desc'] = ''.join(response.xpath('//*[@id="link-report"]/span[@class="all hidden"]/text()').extract())

        yield item

    # def parsr_celebrity(self,response):
    #     pass