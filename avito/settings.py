# -*- coding: utf-8 -*-

# Scrapy settings for avito project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'avito'

SPIDER_MODULES = ['avito.spiders']
NEWSPIDER_MODULE = 'avito.spiders'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "avito"
MONGODB_COLLECTION = "service"

ITEM_PIPELINES = {
  'avito.pipelines.MongoDBPipeline',
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'avito (+http://www.yourdomain.com)'
