# -*- coding: utf-8 -*-
import scrapy
from tianyancha.items import TianyanchaItem
import time


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['tianyancha.com']
    start_urls = ['https://www.tianyancha.com/brand/bc3da74507']

    @staticmethod
    def get_company(response):
        company = TianyanchaItem()
        company['name'] = response.xpath('//*[@id="project_web_top"]/div[2]/div[1]/div/text()')[0].extract()
        company['financing'] = \
            response.xpath('//*[@id="project_web_top"]/div[2]/div[2]/span[1]/text()')[0].extract().split(u'：')[
                1]
        company['created'] = \
            response.xpath('//*[@id="project_web_top"]/div[2]/div[2]/span[2]/text()')[0].extract().split(u'：')[
                1]
        company['local'] = \
            response.xpath('//*[@id="project_web_top"]/div[2]/div[2]/span[3]/text()')[0].extract().split(u'：')[
                1]
        company['desc'] = response.xpath('//*[@id="_container_desc"]/text()')[0].extract()
        return company

    def parse(self, response):
        yield CompanySpider.get_company(response)
        jingpin = response.xpath("//div[@id='_container_jinpin']")[0].xpath('table/tbody/tr')
        try:
            for x in jingpin:
                url = x.xpath('td[2]/table/tbody/tr/td[2]/a/@href')[0].extract()
                yield scrapy.Request(url, meta={'depth': 2}, callback=self.follow_up_parse)
        except Exception:
            pass

    def follow_up_parse(self, response):
        yield CompanySpider.get_company(response)
        print("meta depth:" + str(response.meta['depth']))
        if int(response.meta['depth']) <= 2:
            jingpin = response.xpath("//div[@id='_container_jinpin']")[0].xpath('table/tbody/tr')
            try:
                for x in jingpin:
                    url = x.xpath('td[2]/table/tbody/tr/td[2]/a/@href')[0].extract()
                    print("*" * 20)
                    print("*" * 20)
                    print(u'抛出新url:' + url)
                    print("*" * 20)
                    print("*" * 20)
                    yield scrapy.Request(url, meta={'depth': response.meta['depth'] + 1}, callback=self.follow_up_parse)
            except Exception:
                pass
