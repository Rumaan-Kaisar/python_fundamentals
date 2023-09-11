
# Courses: colt_py_bootcamps    218


# (9-sep-23 for 12-sep-23)

# Courses: colt_py_bootcamps    338 

# --------------    Web Crawler    --------------

# Scrapy: First we need to install scrapy
# pip install Scrapy

    # It's a very powerful FRAMEWWARK for scrapping
        # Scrapy is a fast high-level web crawling and web scraping FRAMEWORK, used to crawl websites and extract structured data from their pages. 
        # It can be used for a wide range of purposes, from 'data mining' to monitoring and 'automated testing'.
        # Documentation: We have to follow the rules for this framework
            # we have to use it in a particular way
            # sacrifice "Flexibility" for "speed" and 'ease of use'



# ---------------    Book Scraper Project    ---------------
# We want to scrape following info mation from: "https://books.toscrape.com/"
            # price
            # title
    # it's a 50 page website, we automate to scrape from all of those page

# creating a spider
    # Spiders are classes which define how a certain site (or a group of sites) will be scraped, including 
        # How to perform the crawl (i.e. follow links) and 
        # How to extract structured data from their pages (i.e. scraping items)

# First analyze a webpage: e.g. amazon
    # Find the HTML structure of each page, dynamically or by scrapping
    # When you get the idea of a single page, you can automate it for the rest of the page
        # it can be done wothout loggong in
        # same does Google: it knowws all the site come-ou with bunch of links
        # Thats why lots of SEO is done with links


# We need to use inheritance, because we'll define a class

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
        response.css('article.product_pod')     # it is similar to soup.select(".special")





################# 7:27 
# copy: book_scraper.py
#       books.csv
#       books2.json

################# (11-sep-23 for 13-sep-23)

# Courses: colt_py_bootcamps    338 

# --------------    Web Crawler    --------------

# Scrapy: First we need to install scrapy
# pip install Scrapy

    # It's a very powerful FRAMEWWARK for scrapping
        # Scrapy is a fast high-level web crawling and web scraping FRAMEWORK, used to crawl websites and extract structured data from their pages. 
        # It can be used for a wide range of purposes, from 'data mining' to monitoring and 'automated testing'.
        # Documentation: We have to follow the rules for this framework
            # we have to use it in a particular way
            # sacrifice "Flexibility" for "speed" and 'ease of use'



# ---------------    Book Scraper Project    ---------------
# We want to scrape following info mation from: "https://books.toscrape.com/"
            # price
            # title
    # it's a 50 page website, we automate to scrape from all of those page

# creating a spider
    # Spiders are classes which define how a certain site (or a group of sites) will be scraped, including 
        # How to perform the crawl (i.e. follow links) and 
        # How to extract structured data from their pages (i.e. scraping items)

# First analyze a webpage: e.g. amazon
    # Find the HTML structure of each page, dynamically or by scrapping
    # When you get the idea of a single page, you can automate it for the rest of the page
        # it can be done wothout loggong in
        # same does Google: it knowws all the site come-ou with bunch of links
        # Thats why lots of SEO is done with links


# We need to use inheritance, because we'll define a class

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
                'price': article.css(".price_color::text")
            }

# ------------    CLI command    ------------
""" 
        > Scrapy 2.10.1 - no active project

        Usage:
        scrapy <command> [options] [args] 
"""

# following CLI command saves data to a csv file
# -----------    save as CSV    -----------
# running in CLI:   scrapy runspider -o books.csv book_scraper.py

# we'll get some list of "objects" in format
# "[<Selector query=""descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' price_color ')]/text()"" data='£51.77'>]"
# We need to extract info from it:
    # since it returns list,  we should use index
    # an alternative wway is to use: extract_first()





# -----------------    mod 2    -----------------

# ----------    extract_first() & RECURSION    ----------
# 'price': article.css(".price_color::text").extract_first()
# 'title': article.css("h3 > a::attr(title)").extract_first()
    # we're usong CSS-selector here

# repeat it for the rest of the page: use "next" button
    # we place following inside the FOR-loop
        # next = response.css('.next > a::attr(href)1).extract_first()
    # and we'l make a recursion:
        # if next:
        #         yield response.follow(next, self.parse)


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

# we can save the data into a JSON file too
# -----------    save as JSON    -----------
# scrapy runspider -o books3.json book_scraper.py





