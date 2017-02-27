# coding:utf-8

from scrapy import cmdline
import time
from datetime import  datetime

print(time.localtime())
print(datetime.fromtimestamp(time.time()))
cmdline.execute("scrapy crawl Team01".split())
