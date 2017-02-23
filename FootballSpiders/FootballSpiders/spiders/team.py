#!/usr/bin/python
#coding:utf-8

import scrapy
from scrapy import Request

from FootballSpiders.items import  *


class TeamSpider(scrapy.Spider):
    name = "Team"
    allowed_domains = ["soccer.hupu.com"]
    start_urls = ['http://soccer.hupu.com/england/',
                  'http://soccer.hupu.com/spain/',
                  'http://soccer.hupu.com/italy/',
                  'http://soccer.hupu.com/germany/'
                  ]

    def parse(self, response):

        items = []

        #urls = response.selector.xpath('//span[@class = "pagnLink"]/a/@href').extract()
        urls=response.selector.xpath('//ul[@class="england-list-item"]/li/a/@href').extract()

        next_links = []
        for url in urls:
            next_links.append(url)

        for url in next_links:
            yield Request(url, callback=self.parse_player)

    def parse_player(self,response):
        items = []
        number=[]
        cn_name=[]
        #item=TeamPlayerItem()

        urls= response.selector.xpath('//table[@class="team_player"]/tr/td/a/@href').extract()
        next_links = []
        for url in urls:
            next_links.append(url)

        for url in next_links:
            yield Request(url, callback=self.parse_player_detail)

    def parse_player_detail(self,response):
        items = []

        parent=response.selector.xpath('//ul[@class="player_detail"]/li')
        item=()
        image=parent[0].xpath('img/@src').extract()
        item['number'] = parent[2].xpath('//span[4]/text()').extract()
        print(image[0])
        url="http:"+image[0]
        item['imageUrl']=url

        item['cn_name'] =parent[1].xpath('//b[1]/text()').extract()
        item['en_name'] =parent[1].xpath('//b[2]/text()').extract()
        item['country'] =parent[1].xpath('//span[1]/text()').extract()
        item['location'] =parent[2].xpath('//span[3]/text()').extract()
        item['birthday'] =parent[1].xpath('//span[2]/text()').extract()
        item['team']=parent[2].xpath('//span[2]/text()').extract()
        items.append(item)
        return items