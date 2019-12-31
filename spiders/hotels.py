import scrapy
import json

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['tez-tour.com']
    country_id = 158976
    page =1
    base_url = f"https://www.tez-tour.com/tariffsearch/getResult?callback=jsonp1577120423047&_=1577120439641&priceMin=0&priceMax=1500000&currency=46688&nightsMin=7&nightsMax=7&hotelClassId=269506&accommodationId=2&rAndBId=15350&tourType=1&locale=ru&cityId=3667&countryId=1104&after=01.06.2020&before=02.06.2020&hotelInStop=false&specialInStop=false&version=2&tourId=1285&tourId=12689&tourId=12706&tourId=143330&tourId=9004247&tourId=70616&tourId=4433&tourId=5736&tourId=139343&tourId=4434&tourId=12691&tourId=21301&tourId=12705&tourId=149827&tourId=4151426&hotelClassBetter=true&rAndBBetter=true&noTicketsTo=false&noTicketsFrom=false&searchTypeId=3&recommendedFlag=false&salePrivateFlag=false&onlineConfirmFlag=false&promoFlag=true&birthdays=&contentCountryId=1102"
    start_urls = [base_url]
    custom_settings = {'FEED_URI': "price.csv",'FEED_FORMAT': "csv"}


    def parse(self, response):
        print("procesing:" + response.url)
        data = {}
        jsonres = json.loads(response.body)
        # total_pages = jsonres['totalPages']
        #
        # if HotelsSpider.page <= total_pages:
        #     HotelsSpider.page += 1
        #     next_page = HotelsSpider.base_url + f'&page={HotelsSpider.page}'
        #     print(next_page)
        #     yield response.follow(next_page, self.parse)

        for item in jsonres['data']:
            for key in item:
                data[key] = item[key]
            yield data







