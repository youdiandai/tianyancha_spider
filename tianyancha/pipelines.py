# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from tools.analysis import str_in_tags
from scrapy.exceptions import DropItem

KEY_WORD = [u'人工智能', u'医疗']


class TianyanchaPipeline(object):
    def __init__(self):
        self.file = codecs.open('scraped_data.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        if str_in_tags(item['tags'], *KEY_WORD):
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line.decode("unicode_escape") + ',')
            return item
        else:
            raise DropItem('Item({}) mismatch'.format(item))

    def open_spider(self, spider):
        self.file = codecs.open('scraped_data.json', 'wb', encoding='utf-8')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write('\n]')
        self.file.close()
