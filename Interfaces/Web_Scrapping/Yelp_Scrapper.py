# -*- coding: utf-8 -*-
import requests
import ssl
from bs4 import BeautifulSoup
import re

class Yelp_Scrapper:
    def __init__(self):
        pass
    
    def scrapper_yelp(self,url):
        number_of_pages=self.get_page_numbers(url)
        reviews = []
        for i in range(0,number_of_pages):
            if i>0:
                url=url+"?start={}".format((i+1)*10)
            headers = {'User-Agent': 'Mozilla/5.0'}
            request = requests.get(url=url, headers=headers)
            html = request.content
            soup = BeautifulSoup(html, 'html.parser')
            html = soup.prettify('utf-8')
            for divs in soup.findAll("p", {"lang": "es"}):
                extracted_review = divs.text.strip()
                reviews.append(extracted_review)
        return reviews

    def get_page_numbers(self,url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = requests.get(url=url, headers=headers)
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify('utf-8')
        pages_number = []
        for divs in soup.findAll("div", {"class": "page-of-pages arrange_unit arrange_unit--fill"}):
            pages= divs.text.strip()
            number = re.findall(r"\d",pages)
            pages_number.append(max(number))
        return int(max(pages_number))

    

