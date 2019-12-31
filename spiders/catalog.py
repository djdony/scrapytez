import scrapy
import json
from ..items import FlexibleItem

class HotelsSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['tez-tour.com']
    country_id = 55359
    page =1
    base_url = f"https://www.tez-tour.com/data/hotels.html?partName=&sortMode=1&countryId={country_id}"
    start_urls = [base_url]
    custom_settings = {'FEED_URI': "sg.csv",'FEED_FORMAT': "csv"}


    def parse(self, response):
        data = FlexibleItem()
        print("procesing:" + response.url)
        jsonres = json.loads(response.body)
        total_pages = jsonres['totalPages']

        if HotelsSpider.page <= total_pages:
            HotelsSpider.page += 1
            next_page = HotelsSpider.base_url + f'&page={HotelsSpider.page}'
            yield response.follow(next_page, self.parse)

        for item in jsonres['hotels']:
            for key in item:
                data[key] = item[key]
            yield data







