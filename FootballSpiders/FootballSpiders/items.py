# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeamItem(scrapy.Item):

    TeamENName=scrapy.Field()
    TeamCNName=scrapy.Field()
    CoachName=scrapy.Field()
    City=scrapy.Field()
    CourtName = scrapy.Field()
    FoundingTime = scrapy.Field()
    ImageUrl = scrapy.Field()
    CourtImage = scrapy.Field()
    Remark = scrapy.Field()
    UpdateTime = scrapy.Field()
    pass

class LeagueItem(scrapy.Item):
    LeagueId = scrapy.Field()
    LeagueName = scrapy.Field()
    ENName = scrapy.Field()
    CountryId = scrapy.Field()
    CountryName = scrapy.Field()
    Levels = scrapy.Field()
    TeamCount = scrapy.Field()
    ContinentName=scrapy.Field()
    EventType = scrapy.Field()
    Remark = scrapy.Field()

    pass


class PlayerItem(scrapy.Item):
    CNName = scrapy.Field()
    ENName = scrapy.Field()
    Status = scrapy.Field()
    TeamName = scrapy.Field()
    TeamId = scrapy.Field()
    CountryID = scrapy.Field()
    CountryName=scrapy.Field()
    Birthday = scrapy.Field()
    BodyWeight = scrapy.Field()
    Height = scrapy.Field()
    Position = scrapy.Field()
    Number = scrapy.Field()
    ImageUrl = scrapy.Field()
    pass

