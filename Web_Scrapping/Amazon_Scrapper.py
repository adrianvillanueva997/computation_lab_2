import re

import requests
from bs4 import BeautifulSoup


class Amazon:
    def __init__(self):
        pass

    @staticmethod
    def make_request(url):
        """
        TODO Hacer que el scraper cambie de la página del producto a la página de los comentarios.
        TODO Revisar por que a veces no saca reviews y el numero aleatorio de reviews.
        TODO Retocar el scraper de Metacritic.
        TODO Sacar reviews por puntuación.
        """
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

    def get_divs(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.findAll("div", {"class": "a-section review aok-relative",
                                    "data-hook": "review"})
        return divs

    def extract_reviews_from_divs(self, divs):
        reviews = []
        for div in divs:
            div = str(div)
            soup = BeautifulSoup(div, 'html.parser')
            review_body = soup.find('span', {
                'class': 'a-size-base review-text review-text-content', 'data-hook': 'review-body'})
            regex = r'<[^>]*>'
            review = re.sub(regex, '', str(review_body))
            reviews.append(review)
        return reviews

    def change_to_comments(self, url):
        regex = r'\/dp\/'
        replace = 'product-reviews'
        url = url.replace(regex, replace)
        return url

    def amazon_scraper(self, url):
        # * Transformar url de pagina de producto a comentarios aqui!
        comments_url = self.change_to_comments(url)
        number_page = 1
        max_page = 2
        total_reviews = []
        while number_page < max_page:
            url_modified = comments_url + '&pageNumber=' + str(number_page)
            html = self.make_request(url_modified)
            divs = self.get_divs(html)
            reviews = self.extract_reviews_from_divs(divs)
            if len(reviews) is 0:
                number_page = max_page
            else:
                for review in reviews:
                    total_reviews.append(review)
                    print(review)
                number_page += 1
                max_page += 1
        return total_reviews


if __name__ == '__main__':
    amz = Amazon()
    urls = 'https://www.amazon.es/Sony-Dualshock-Edici%C3%B3n-Limitada-oscuro/dp/B07GBLZLT7?pd_rd_wg=VIrhd&pd_rd_r=ebd13114-0e29-4cff-a180-4b9981acdfd9&pd_rd_w=puiFr&ref_=pd_gw_ri&pf_rd_r=D7WYJPS59CH9S6Q4PT8W&pf_rd_p=c5aee406-5d18-5b65-ae10-767a4ba1ae1f'
    amz.amazon_scraper(urls)
