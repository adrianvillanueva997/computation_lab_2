import re

import requests
from bs4 import BeautifulSoup
import abc
from Modules.Web_Scrapping.Scrapper import Scrapper


class Metacritic_Scrapper(Scrapper):
    def __init__(self):
        pass

    @staticmethod
    def __make_request(url):
        """
        Recieves an url and returns the raw html code of a webpage.
        :returns html: str
        :argument url: str
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}
        request = requests.get(url=url, headers=headers)
        print(f'[INFO] Request made to: {url} with response: {request}')
        html = request.content
        return html

    @staticmethod
    def __get_divs(html):
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.findAll('div', {'class': 'review_section'})
        return divs

    @staticmethod
    def __get_reviews(divs):
        reviews = []
        for div in divs:
            soup = BeautifulSoup(str(div), 'html.parser')
            review = soup.find('div', {'class': 'review_body'})
            regex = r'<[^>]*>'
            review_scraped = re.sub(regex, '', str(review))
            review_scraped = review_scraped.replace('None', '')
            review_scraped = (review_scraped.strip())
            reviews.append(review_scraped)

        return reviews

    def metacritic(self, url):
        html = self.__make_request(url + '/user-reviews')
        divs = self.__get_divs(html)
        review_list = []
        reviews = self.__get_reviews(divs)
        num_page = 1
        max_page = 2
        for review in reviews:
            review_list.append(review)
        while num_page < max_page:
            new_url = url + '/user-reviews' + f'?page={str(num_page)}'
            html = self.__make_request(new_url)
            divs = self.__get_divs(html)
            reviews = self.__get_reviews(divs)
            print(len(reviews))
            if len(reviews) == 5:
                num_page = max_page
            else:
                for review in reviews:
                    review_list.append(review)
                print(len(review_list))
                num_page += 1
                max_page += 1
        print(review_list)
        return review_list


if __name__ == '__main__':
    ms = Metacritic_Scrapper()
    # ms.metacritic(url=r'https://www.metacritic.com/game/pc/dota-2')
    ms.metacritic(url=r'https://www.metacritic.com/game/pc/team-fortress-2')
