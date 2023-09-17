# -*- coding: utf-8 -*-
import os

from lazy_crawler.lib.user_agent import get_user_agent

BOT_NAME = "lazy_py_crawler"

SPIDER_MODULES = ["lazy_crawler.crawler.spiders"]
NEWSPIDER_MODULE = "lazy_crawler.crawler.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

    
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16

CONCURRENT_REQUESTS_PER_IP = 16

# Enable the HttpProxyMiddleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
} 

# Configure the HttpProxyMiddleware
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'lazy_crawler.crawler.pipelines.DarazDBPipeline': 300,
    }

DOWNLOAD_DELAY = 0

################################################################
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 429, 430]
# 
RETRY_ENABLED = True

RETRY_TIMES = 3  # Maximum number of times to retry a request

USER_AGENT = get_user_agent('random')

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"