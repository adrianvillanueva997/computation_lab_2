import requests
from bs4 import BeautifulSoup
import re


class Amazon:
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
    def __get_div_blocks(html):
        """
        Recieves the raw html code and returns a list with the div class blocks that we want.
        :returns div_class_blocks: list
        :argument url: str
        """
        soup = BeautifulSoup(html, 'html.parser')
        div_class_blocks = soup.findAll("div", class_='a-section celwidget')
        return div_class_blocks

    @staticmethod
    def __check_limit(html):
        soup = BeautifulSoup(html, 'html.parser')
        limit = soup.find('div', {'class': 'a-section a-spacing-top-large a-text-center no-reviews-section'})
        limit = str(limit).replace(
            '<div class="a-section a-spacing-top-large a-text-center no-reviews-section"><span class="a-size-medium">',
            '')
        if len(limit) == 4:
            return True
        else:
            return False

    @staticmethod
    def __filter_data(div_blocks):
        """
        Recieves a list of div classes and filters the reviews by the rating score, returns a dictionary with 3 lists, one for each kind of review.
        :returns datos : dict
        :argument div_blocks: list
        """
        # malas: 1-2
        # neutras: 3
        # buenas: 4-5
        datos = {
            'malas': [],
            'neutras': [],
            'buenas': []
        }
        for block in div_blocks:
            soup = BeautifulSoup(str(block), 'html.parser')
            regex = r'<i.*\"'
            rating = soup.find('i', {'data-hook': 'review-star-rating'})
            rating = str(rating).replace('<span class="a-icon-alt">', '')
            rating = re.sub(regex, '', rating)
            rating = rating.replace(',0 de 5 estrellas</span></i', '')
            rating = rating.replace('>', '')
            rating = int(rating)

            review = soup.find('span', {'class': 'cr-original-review-content'})
            review = str(review).replace('<span class="cr-original-review-content">', '')
            review = review.replace('<br/>', '')
            review = review.replace('</span>', '')

            if rating == 1 or rating == 2:
                datos['malas'].append(review)
            elif rating == 3:
                datos['neutras'].append(review)
            elif rating == 4 or rating == 5:
                datos['buenas'].append(review)

        print(datos)
        return datos

    def scrape_amazon(self, urls_list):
        data = {
            'malas': [],
            'neutras': [],
            'buenas': []
        }
        for url in urls_list:
            num_page = 1
            max = 2
            while num_page < max:
                html = self.__make_request(
                    url + 'cm_cr_arp_d_paging_btm_' + str(num_page) + '?pageNumber=' + str(num_page))
                blocks = self.__get_div_blocks(html)
                if self.__check_limit(html):
                    filtered_data = self.__filter_data(blocks)
                    for malas in filtered_data['malas']:
                        data['malas'].append(malas)
                    for neutras in filtered_data['neutras']:
                        data['neutras'].append(neutras)
                    for buenas in filtered_data['buenas']:
                        data['buenas'].append(buenas)
                    num_page += 1
                    max += 1
                else:
                    num_page = max
        return data


if __name__ == '__main__':
    amz = Amazon()
    urls = ['https://www.amazon.es/New-Super-Mario-Bros-Deluxe/product-reviews/B07HD1312V/']
    data = amz.scrape_amazon(urls)
    print(data)
