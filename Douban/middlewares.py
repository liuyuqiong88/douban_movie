import random

from scrapy import Request

# from Douban.settings import USER_AGENTS
from scrapy.conf import settings

class RandomProxy(object):


    def process_request(self,request,spider):

        request.meta['proxy'] = '180.121.131.34:8181'


class RandomUserAgent(object):


    def process_request(self,request,spider):

        # request.meta['proxy'] = '119.62.227.90:61202'

        ua = random.choice(settings['USER_AGENTS'])
        request.headers['User-Agent'] = ua
        # print('2222222222222222222222222222222222222222', settings['USER_AGENTS'])

        pass

