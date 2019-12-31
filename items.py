# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class TezItem(scrapy.Item):
#     # define the fields for your item here like:
#     id = scrapy.Field()
#     pass

class FlexibleItem(scrapy.Item):
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        super(FlexibleItem, self).__setitem__(key, value)
