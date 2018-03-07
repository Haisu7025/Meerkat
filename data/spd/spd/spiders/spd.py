import re
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.selector import Selector


class spd(scrapy.Spider):
    name = 'spd'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zone-h.org/archive/special=1/page=1?zh=1"
    }

    def start_requests(self):
        return [Request("http://www.zone-h.org/archive/special=1/page=1", method='GET', headers=self.headers, callback=self.parse)]

    def parse(self, response):
        print response.text
        titles = response.xpath(
            '//*[@id="ldeface"]/tbody/tr[2]/td[8]').extract()
        for title in titles:
            print title
