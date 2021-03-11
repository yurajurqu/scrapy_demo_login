# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class OpenlibrarySpider(scrapy.Spider):
    name = 'openlibrary'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid='register',
            formdata={
                'username': 'yyyyyy',
                'password': 'xxxxxxx',
                'redirect': '/',
                'debug_token': '',
                'login':'Log In'
            },
            callback=self.after_login
        )
    def after_login(self, response):
        print('after login')