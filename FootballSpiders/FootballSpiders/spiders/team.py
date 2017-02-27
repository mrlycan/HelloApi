#!/usr/bin/python
#coding:utf-8

import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import FootballSpiders.items as items
import re


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

class TeamS01pider(CrawlSpider):
    name = 'Team01'
    allowed_domains = ["soccer.hupu.com"]
    start_urls = ['https://soccer.hupu.com/teams/'
                  ]

    rules = (
        Rule(LinkExtractor(allow=(r'https://soccer.hupu.com/teams/121',)), callback='parse_team01'),
        Rule(LinkExtractor(allow=(r'https://soccer.hupu.com/g/players/[a-z]-\d.html"',)),callback='parse_player'),
    )

    def parse_team01(self,response):
        tempItems = []

        item = items.TeamItem()

        # 截取球员信息url
        playerUrls = response.selector.xpath('//table[@class="team_player"]/tr/td/a/@href').extract()
        next_links = []
        for url in playerUrls:
            next_links.append(url)

        parent = response.selector.xpath('//div[@class="team_info left"]')[0]

        name = parent.xpath('h3/span/text()').extract()[0]
        if len(name) > 0:
            cnname = re.findall(r'[\u4e00-\u9fa5]+', name)
            enname = re.findall(r'[^\u4e00-\u9fa5]+', name)
            item['TeamENName'] = enname[0].strip() if len(enname) > 0 else ''
            item['TeamCNName'] = cnname[0].strip() if len(cnname) > 0 else ''

        Coach=parent.xpath('//dl[@class="clearfix"]/dd[1]/text()').extract()[0].split('：')
        item['CoachName'] =Coach[1].strip() if len(Coach)>1 else ''
        City= parent.xpath('//dl[@class="clearfix"]/dd[3]/text()').extract()[0].split('：')
        item['City'] =City[1].strip() if len(City)>1 else ''
        Court=parent.xpath('ul[2]/li[1]/text()').extract()[0].split('：')
        item['CourtName'] = Court[1].strip() if len(Court)>1 else ''

        image=parent.xpath('ul[1]/li[@class=" left pic_logo"]/img/@src').extract()
        if len(image)>0:
            item['ImageUrl']='https:'+image[0]
        item['Remark']=''
        yield item
        for url in next_links:
            yield Request(url, callback=self.parse_player)

    def parse_player(self,response):
        item = items.PlayerItem()
        parent=response.selector.xpath('//ul[@class="player_detail"]')
        CNName=parent.xpath('li[@class="center"]/b[1]/text()').extract()
        item['CNName']=CNName[0] if len(CNName)>0 else ''

        ENName=parent.xpath('li[@class="center"]/b[2]/text()').extract()
        item['ENName'] = ENName[0] if len(ENName) > 0 else ''

        CountryName=parent.xpath('li[@class="center"]/span[1]/text()').extract()
        item['CountryName'] = CountryName[0] if len(CountryName) > 0 else ''
        Birthday = parent.xpath('li[@class="center"]/span[2]/text()').extract()
        item['Birthday'] = Birthday[0] if len(Birthday) > 0 else ''
        BodyWeight=parent.xpath('li[@class="center"]/span[3]/text()').extract()
        item['BodyWeight'] = BodyWeight[0] if len(BodyWeight) > 0 else ''

        Height=parent.xpath('li[3]/span[1]/text()').extract()
        item['Height'] = Height[0] if len(Height) > 0 else ''

        TeamName = parent.xpath('li[3]/span[2]/a/text()').extract()
        item['TeamName'] = TeamName[0] if len(TeamName) > 0 else ''

        Position = parent.xpath('li[3]/span[3]/text()').extract()
        item['Position'] = Position[0] if len(Position) > 0 else ''

        Number=parent.xpath('li[3]/span[4]/text()').extract()
        item['Number'] = Number[0] if len(Number) > 0 else ''
        yield item