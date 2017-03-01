# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import pymysql
import time
import FootballSpiders.items as items
from datetime import datetime

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
        self.cursor.connection()

        if isinstance(item,items.PlayerItem):
            print('PlayerItem')
            self.PlayerItemAdd(item)
        if isinstance(item,items.TeamItem):
            print('Team')
            self.TeamItemAdd(item)

        self.cursor.close()
        self.connection.close()
        return  item

    def TeamItemAdd(self,item):
        sql='insert into league_team(ENName,CNName,CoachName,CourtName,ImageUrl,Remark,UpdateTime) VALUES(%s,%s,%s,%s,%s,%s,%s)'

        try:
            self.cursor.execute(sql,(
                item['TeamENName'],
                item['TeamCNName'].encode('utf-8'),
                item['CoachName'].encode('utf-8'),
                item['CourtName'].encode('utf-8'),
                item['ImageUrl'].encode('utf-8'),
                item['Remark'].encode('utf-8'),
                datetime.fromtimestamp(time.time())
                ))
            self.connection.commit()
            item['id']=int(self.cursor.lastrowid)

        except pymysql.Error as e:
            print(e.args)
        return  item

    def PlayerItemAdd(self,item):
        sql='INSERT into league_player(CNName,ENName,Status,TeamId,TeamName,CountryName,Birthday,BodyWeight,Height,Position,Number,ImageUrl)' \
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            self.cursor.execute(sql,(
                item['CNName'].encode('utf-8'),
                item['ENName'],
                0,
                item['TeamId'],
                item['TeamName'],
                item['CountryName'].encode('utf-8'),
                datetime.strptime(item['Birthday'], '%Y-%m-%d'),

                item['BodyWeight'],
                item['Height'],
                item['Position'],
                item['Number'],
                item['ImageUrl']
            ))
            self.connection.commit()
            item['id'] = int(self.cursor.lastrowid)

        except pymysql.Error as e:
            print(e.args)
        return item

