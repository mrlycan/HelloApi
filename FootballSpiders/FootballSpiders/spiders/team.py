#!/usr/bin/python
#coding:utf-8

import scrapy
from scrapy import Request
import re
import FootballSpiders.items as items


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
            yield Request(url, callback=self.parse_team)

    def parse_team(self,response):
        tempItems = []

        item=items.TeamItem()

        #截取球员信息url
        playerUrls= response.selector.xpath('//table[@class="team_player"]/tr/td/a/@href').extract()
        next_links = []
        for url in playerUrls:
            next_links.append(url)

        parent=response.selector.xpath('//div[ @class="team_info left"]')[0]

        name=parent.xpath('h3/span/text()').extract()[0]
        if len(name)>0:
            cnname=re.findall(r'[\u4e00-\u9fa5]+',name)
            enname=re.findall(r'[^\u4e00-\u9fa5]+',name)
            item['TeamENName']=enname[0].strip() if len(enname)>0 else ''
            item['TeamCNName']=cnname[0].strip() if len(cnname)>0 else ''

        coach=parent.xpath('//dl[@class="clearfix"]/dd[1]/text()').extract()[0]
        city=parent.xpath('//dl[@class="clearfix"]/dd[3]/text()').extract()[0]
        court=parent.xpath('ul[2]/li[1]/text()').extract()[0]
        for url in next_links:
            yield Request(url, callback=self.parse_player)
        #return tempItems
    def parse_player(self,response):
        tempItems = []

        parent=response.selector.xpath('//ul[@class="player_detail"]/li')
        item=items.PlayerItem()
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
        tempItems.append(item)
        return items