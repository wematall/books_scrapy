import scrapy

class BookSpider(scrapy.Spyder):
    name = "BookSpyder"
    start_urls = ["https://knigi.tomsk.ru/products/new"]
    
    def parse(self, response):
        links = response.css("div.name a::attr(href)")
        for link in links:
            yield response.follow(link, self.parse_book)
        pass

    def parse_book(self, response):
        yield {
            "name": response.css("div.page h1::text").get(),
            "price": response.css("div.price-helper div.price::text").get(),
            "genre": response.css("div.breadcrumbs ul li a::text")[-1].get()
        }
        # product_name = response.css("div.page h1::text").get()
        # product_price = response.css("div.price-helper div.price::text").get()
        # product_genre = response.css("div.breadcrumbs ul li a::text")[-1].get()

        # response.css("div.name a::attr(href)")

        pass