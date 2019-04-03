import re

import requests
from bs4 import BeautifulSoup


class Metacritic_Scrapper:
    def __init__(self):
        pass

    @staticmethod
    def __make_request(url):
        """
        Recieves an url and returns the raw html code of a webpage.
        :returns html: str
        :argument url: str
        """
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = requests.get(url=url, headers=headers)
        print(f'[INFO] Request made to: {url} with response: {request}')
        html = request.content
        return html

    @staticmethod
    def __div_blocks(html):
        """
        Scrapes each of the review body found in the HTML string.
        :param html:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        div_reviews = soup.findAll('div', {'class': 'review_body'})
        return div_reviews

    @staticmethod
    def __get_comments(div_blocks):
        """
        Receives a list with review bodies and cleans and extracts the reviews and saves them in a list.
        :param div_blocks:
        :return:
        """
        reviews = []
        for block in div_blocks:
            soup = BeautifulSoup(str(block), 'html.parser')
            review = soup.find('span', {'class': 'blurb blurb_expanded'})
            if review is not None:
                regex = r'<[^>]*>'
                review = re.sub(regex, '', str(review))
                reviews.append(review)

        return reviews

    def scrape_metacritic(self, urls):
        """
        Public method that extracts all the reviews given a list of Metacritic URLS
        :param urls:
        :return:
        """
        data = []
        for url in urls:
            start = 0
            next = 1
            while start < next:
                html = self.__make_request(url + f'user-reviews?page={str(start)}')
                blocks = self.__div_blocks(html)
                reviews = self.__get_comments(blocks)
                if len(reviews) is 0:
                    start = next
                else:
                    for review in reviews:
                        data.append(review)
                    start += 1
                    next += 1
        return data


if __name__ == '__main__':
    yt = Metacritic_Scrapper()
    urls = ['https://www.metacritic.com/game/pc/dota-2/']
    a = yt.scrape_metacritic(urls)
    print(len(a))
