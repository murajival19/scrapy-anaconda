# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3

class CheckItemPipeline:
    def process_item(self, item, spider):
        if not item.get('isbn'):
            raise DropItem('Missing ISBN')
        return item

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('BOOKDB.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE computer_books(
                    title text,
                    author text,
                    price integer,
                    publisher text,
                    size text,
                    page integer,
                    isbn text primary key
                )  
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
        
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO computer_books(title, author, price, publisher, size, page, isbn)
            VALUES(?,?,?,?,?,?,?)
        ''', (
            item.get('title'),
            item.get('author'),
            item.get('price'),
            item.get('publisher'),
            item.get('size'),
            item.get('page'),
            item.get('isbn')
        ))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()