from scrapy import signals
import datetime
import os
import django
from pathlib import Path
import sys
from django.db import transaction
from django.db.utils import IntegrityError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

sys.path.append(str(BASE_DIR))  # Add the base directory to the PYTHONPATH

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from products.models import Product

class DarazDBPipeline(object):
    def __init__(self):
        self.created_time = datetime.datetime.now()

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        pass
    
    @transaction.atomic
    def process_item(self, item, spider):
        name = item.get('name')
        rating = item.get('rating')
        price = item.get('price')
        reviews = item.get('reviews')
        sold_by = item.get('sold_by')
        category = item.get('category')
        productUrl = item.get('productUrl')
        
        ###now save the product

        try:
          Product.objects.create(
                name=name,
                rating=rating, 
                price = price,
                reviews=reviews,
                sold_by=sold_by,
                category=category,
                productUrl=productUrl
                )
        except IntegrityError as e :
            print('Already save in db')

        return 'successfully save in db.'
    

