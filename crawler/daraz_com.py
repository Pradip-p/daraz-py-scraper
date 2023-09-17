#!/usr/bin/env python
import os
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lazy_crawler.crawler.spiders.base_crawler import LazyBaseCrawler
from lazy_crawler.lib.user_agent import get_user_agent
import gc
from lxml import html
import json


class LazyCrawler(LazyBaseCrawler):
    
    name = "www_daraz_com_np"

    allowed_domains = ['daraz.com.np']

    custom_settings = {
        'DOWNLOAD_DELAY': 2,'LOG_LEVEL': 'DEBUG',
        
        'CONCURRENT_REQUESTS' : 1,'CONCURRENT_REQUESTS_PER_IP': 1,

        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,'RETRY_TIMES': 2,

        'ITEM_PIPELINES' :  {
            'lazy_crawler.crawler.pipelines.DarazDBPipeline': 300
        }
    }


    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def start_requests(self): #project start from here.
        headers = {
            'User-Agent': get_user_agent('random'),
            **self.HEADERS,  # Merge the HEADERS dictionary with the User-Agent header
            }
        urls = [
            'https://www.daraz.com.np/womens-clothing/',
            'https://www.daraz.com.np/womens-sarees/'
            #add on below for other category urls
        ]
        for url in urls:
            
            yield scrapy.Request(url, self.parse_url, dont_filter=True,
                    headers= headers,
                    )
    

    def parse_url(self, response):
        tree = html.fromstring(response.text)
        # Use XPath to select the 4th script tag
        script_tags = tree.xpath('//script')
        # Check if there are at least four script tags
        if len(script_tags) >= 4:
            # Extract the content of the 4th script tag
            data = script_tags[3].text
            # print(data)
            # Extract the JSON data from the string
            start_index = data.find('{')  # Find the first '{' character
            
            json_data = data[start_index:]

            # Load the JSON data
            parsed_data = json.loads(json_data)

            listItems = parsed_data['mods']['listItems']
            category = parsed_data['mods']['filter']['filterItems'][0]['value']
            for item in listItems:
                yield {
                    'name': item.get('name'),
                    'rating': item.get('ratingScore'),
                    'price': item.get('priceShow'),
                    'reviews': item.get('review'),
                    'sold_by': item.get('sellerName'),
                    'category': category,
                    'productUrl': item.get('productUrl')
                }
                
            # Extract the page number from the JSON data
            current_page = parsed_data["mainInfo"]["page"]
                # Calculate the next page number
            next_page = int(current_page) + 1
            pageSize = int(parsed_data["mainInfo"]["pageSize"])
            if next_page<= pageSize:
                # Construct the next page URL
                # next_page_url = f'{response.url}?page={next_page}'
                next_page_url = f'{response.url.split("?")[0]}?page={next_page}'
                # You can yield a Request to the next page URL for further scraping
                yield scrapy.Request(url=next_page_url, callback=self.parse_url, dont_filter=True)
        else:
            print('There are fewer than 4 script tags on the page.')


        gc.collect()

settings_file_path = 'lazy_crawler.crawler.settings'
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
process = CrawlerProcess(get_project_settings())  
process.crawl(LazyCrawler)
process.start() # the script will block here until the crawling is finished