
import scrapy

# inheriting from scrapy.Spider
class BookSpider(scrapy.Spider):
    name = "bookspider"
    # list of urls we want to scrap
    start_urls = ['https://books.toscrape.com/']

    # parse: it is required for every 'spider'
        # it parse the result of the request, it invokes "requests" autometically
        # parse is called over & over depend on how we define 'parse':
            # it called on every single response it gets back, when we scrape
        # response: the thing we get from the http requests
    def parse(self, response):
        # response.css('article.product_pod')     # it is similar to soup.select(".special")
        for article in response.css('article.product_pod'):
            yield { # we have to use 'yield' (instead of return), it goes over n over
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)

# scrapy runspider -o books.csv book_scraper.py
# or save data as JSON
# scrapy runspider -o books.json book_scraper.py

