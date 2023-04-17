import scrapy
import time

class BookSpider(scrapy.Spider):
    name = "BookSpyder"
    start_urls = ["http://knigi.tomsk.ru/products/new"]
    
    def parse(self, response):
        links = response.css("div.name a::attr(href)")
        for link in links:
            time.sleep(3)
            yield response.follow(link, self.parse_book)
        
        link = response.css("div.pagination a::attr(href)")[-1].get()
        yield response.follow(link, self.parse)

    def parse_book(self, response):
        yield {
            "name": response.css("div.page h1::text").get().split(",")[0].strip(),
            "price": response.css("div.price-helper div.price::text").get().split("Р")[0].strip(),
            "genre": response.css("div.breadcrumbs ul li a::text")[-1].get()
        }
        # product_name = response.css("div.page h1::text").get()
        # product_price = response.css("div.price-helper div.price::text").get().split("P")[0].strip()
        # product_genre = response.css("div.breadcrumbs ul li a::text")[-1].get()

        # response.css("div.name a::attr(href)")

        pass