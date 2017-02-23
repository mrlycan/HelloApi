import scrapy
from FootballSpiders.items import  *
from  scrapy import Request

class LeagueSpider(scrapy.Spider):
    name = "league"

    start_urls = [
        'https://soccer.hupu.com/teams/'
    ]

    def parse(self, response):
        items = []

        row = []
        teamUrls = response.selector.xpath("//div[@class='bd']/table/tr/td/a/@href").extract()
        for url in teamUrls:
            yield Request(url, callback=self.parse_team())

    def parse_team(self,response):
        items=[]




