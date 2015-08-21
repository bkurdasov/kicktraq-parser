# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import MapCompose, Join

def filter_rn(string):
    return string.replace('\n',' ').replace('\r','').strip()

class KicktraqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project = scrapy.Field(
        input_processor=MapCompose(filter_rn),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=MapCompose(filter_rn),
        output_processor=Join(),
    )
    category = scrapy.Field(
        input_processor=MapCompose(filter_rn),
        output_processor=Join(),
    )
    subcategory = scrapy.Field(
        input_processor=MapCompose(filter_rn),
        output_processor=Join(),
    )
    status = scrapy.Field(
        input_processor=MapCompose(filter_rn),
        output_processor=Join(),
    )

    '''
    backers = scrapy.Field()
    raised = scrapy.Field()
    goal = scrapy.Field()
    avg_daily_funding = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    '''
