# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import pymysql
import time
import FootballSpiders.items as items


db_config={
    'host':'43.254.217.147',
    'port':13306,
    'user':'hello',
    'password':'passw0rd',
    'db':'test',
    'charset':'utf8'
}
class FootballspidersPipeline(object):
    #def __init__(self):
        #self.file = codecs.open('CSDNBlog_data.json', mode='wb', encoding='utf-8')
    def process_item(self, item, spider):
        return item

class TeamPipeline(object):
    def __init__(self):
        self.connection =connection=pymysql.connect(**db_config)
        self.cursor=self.connection.cursor()
        #self.file = codecs.open('CSDNBlog_data.json', mode='wb', encoding='utf-8')
    def process_item(self, item, spider):

        if isinstance(item,items.PlayerItem):
            print('PlayerItem')
        if isinstance(item,items.TeamItem):
            print('Team')
            self.TeamItemAdd(item)
        return  item

    def TeamItemAdd(self,item):
        sql='insert into league_team(TeamId,TeamENName,TeamCNName,CoachName,CourtName,ImageUrl,Remark,UpdateTime) VALUES(%$,%$,%$,%$,%$,%$,%$,%$)'

        try:
            self.cursor.execute(sql,(
                1,
                item['TeamENName'],
                item['TeamCNName'].encode('utf-8'),
                item['CoachName'].encode('utf-8'),
                item['CourtName'].encode('utf-8'),
                item['ImageUrl'].encode('utf-8'),
                item['Remark'].encode('utf-8'),
                time.time()
                ))
        except pymysql.Error as e:
            print(e.args)
        return  item



