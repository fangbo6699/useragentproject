# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UseragentprojectItem(scrapy.Item):
        # define the fields for your item here like:
        ua_name = scrapy.Field()
        ua_string = scrapy.Field()