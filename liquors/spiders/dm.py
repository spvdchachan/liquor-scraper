import re

from scrapy.spiders import SitemapSpider
from scrapy import Request


class DMSpider(SitemapSpider):
    name = 'danmurphys'
    allow_domains = ['danmurphys.com.au']
    sitemap_urls = ['https://www.danmurphys.com.au/sitemap/ProductSitemap.xml']
    sitemap_rules = [
        ('/product/', 'parse_product')
    ]

    def parse_product(self, response):
        product_id = re.findall('(?<=DM_).{1,}(?=/)',
                                response.url)[0]
        self.logger.info('Product ID', product_id)
        yield Request(f'https://api.danmurphys.com.au/apis/ui/'
                      'Product/{product_id}',
                      self.parse_product_api)

    def parse_product_api(self, response):
        self.logger.info(response.text)
