# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class TezPipeline(object):

    def __init__(self):
        self.connection()
        self.create_table()

    def connection(self):
        self.conn = sqlite3.connect('db.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS hotels''')
        self.curr.execute('''
                            create table hotels(
                            data text,
                            )
                            ''')


    def process_item(self, item, spider):
        self.store(item)

        #print("Pipeline :" + item['name'])
        return item
    def store(self, item):
        self.curr.execute('''insert into hotels values (?)''',(item))
        self.conn.commit()