# -*- coding: utf-8 -*-
import scrapy
from useragentproject import items

class UseragentSpider(scrapy.Spider):
    name = 'useragent'
    allowed_domains = ["useragentstring.com"]
    start_urls = (
        'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox',
        'http://www.useragentstring.com/pages/useragentstring.php?name=Internet+Explorer',
        'http://www.useragentstring.com/pages/useragentstring.php?name=Opera',
        'http://www.useragentstring.com/pages/useragentstring.php?name=Safari',
        'http://www.useragentstring.com/pages/useragentstring.php?name=Chrome',
    )

    # 在所有的请求发生之前执行
    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        ua_name = response.url.split('=')[-1]
        for ua_string in response.xpath('//li/a/text()').extract():
            item = items.UseragentprojectItem()
            item['ua_name'] = ua_name
            print(ua_name)
            item['ua_string'] = ua_string.strip()
            print(ua_string.strip())
            yield item
