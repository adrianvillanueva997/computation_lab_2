# -*- coding: utf-8 -*-
import requests
import ssl
from bs4 import BeautifulSoup

class Yelp_Scrapper:
    def __init__(self):
        pass
    
    def scrapper_yelp(self,url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = requests.get(url=url, headers=headers)
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify('utf-8')
        reviews = []
        for divs in soup.findAll("p", {"lang": "es"}):
            extracted_review = divs.text.strip()
            reviews.append(extracted_review)
        return reviews

    
   
   
