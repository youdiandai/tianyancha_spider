# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from selenium import webdriver
import time


class TianyanchaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TianyanchaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        self.browser = webdriver.Chrome('/Users/changxin/Documents/chromedriver')
        # self.browser = webdriver.PhantomJS()
        self.browser.get('https://www.tianyancha.com')
        time.sleep(2)
        a = self.browser.find_element_by_xpath('//*[@id="web-content"]/div/div[1]/div[1]/div/div/div[2]/div/div[4]/a')
        a.click()
        b = self.browser.find_elements_by_xpath("//div[@tyc-event-ch='LoginPage.PasswordLogin']")[0]
        for x in range(10):
            b.click()
        login_form = self.browser.find_elements_by_class_name("modulein1")[0]
        tel = login_form.find_elements_by_xpath("div[2]/input")[0]
        tel.send_keys("16601117967")
        passwd = login_form.find_element_by_class_name('contactword')
        passwd.send_keys("aizai2017")
        btn = login_form.find_element_by_class_name('btn-primary')
        btn.click()
        self.browser.get('https://www.tianyancha.com/brand/bc3da74507')

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        time.sleep(2)
        self.browser.get(request.url)
        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                            status=200)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
