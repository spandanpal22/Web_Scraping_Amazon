# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#using MongoDB to store the scrapped data
import pymongo

class AmazonscrapingPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(    # set your own parameters here
            'localhost',
            27017
        )
        db = self.conn['myproducts']  # creating database with name myproducts
        self.collection = db['products_tb']  # creating table products_tb

    def process_item(self, item, spider):  # item variable will contain our scrapped data
        self.collection.insert(dict(item))
        # print("Pipeline : "+item['product_name'][0])

        return item
