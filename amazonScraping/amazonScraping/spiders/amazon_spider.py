# -*- coding: utf-8 -*-

# We are scraping Amazon site here. I have used USER_AGENT also to bypass restrictions by Amazon.

# I have also set up the pipeline to store the scrapped data in a MongoDB database

import scrapy
from ..items import AmazonscrapingItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2

    # I am here scrapping books' name,author,price and image link.
    # You can change the link as per your need and further choose the CSS selectors as per your requirement
    start_urls = [
        'https://www.amazon.in/s?k=books&page=1&qid=1586697727&ref=sr_pg_2'
    ]

    def parse(self, response):
        items = AmazonscrapingItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_image = response.css('.s-image-fixed-height .s-image').css('::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield items

        next_page = 'https://www.amazon.in/s?k=books&page=' + str(
            AmazonSpiderSpider.page_number) + '&qid=1586697727&ref=sr_pg_2'

        max_page = 3  # set up the maximum number of pages you want to scrape

        if AmazonSpiderSpider.page_number <= max_page:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
