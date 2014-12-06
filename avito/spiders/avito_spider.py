import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from avito.items import AvitoItem

class AvitoSpider(Spider):
    name = "avito"
    allowed_domains = ["avito.ru"]
    start_urls = [
        "https://www.avito.ru/mahachkala/uslugi",
        #"https://www.avito.ru/mahachkala/rabota",
    ]


    def parse(self, response):
        for sel in response.xpath("//div[@class='description']"):
            item = AvitoItem()
            item['title'] = sel.xpath('h3/a/text()').extract()
            item['date'] = sel.xpath('div[@class]').extract()
            yield item






