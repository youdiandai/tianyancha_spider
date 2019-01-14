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
        self.companies = []

    def process_item(self, item, spider):
        if str_in_tags(item['tags'], *KEY_WORD):
            # line = json.dumps(dict(item)) + '\n'
            # self.file.write(line.decode("unicode_escape") + ',')
            self.companies.append(dict(item))
            return item
        else:
            raise DropItem('Item({}) mismatch'.format(item))

    def close_spider(self, spider):
        with codecs.open('scraped_data.json', 'wb', encoding='utf-8') as f:
            json.dump(self.companies, f, indent=4, ensure_ascii=False)
        # self.file.write(json.dumps(self.companies).decode("unicode_escape"))
        # self.file.close()
