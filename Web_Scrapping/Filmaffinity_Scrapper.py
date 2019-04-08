import re

import requests
from bs4 import BeautifulSoup


class Filmaffinity:
    def __init__(self):
        pass

    @staticmethod
    def change_urls(url):
        id = "/"
        new_id = url.split(id)[4].replace('film', '')
        print('newid ' + new_id)
        replacement = "/reviews/1/"
        new_url = url.replace("/film", replacement)
        print('newURL ' + new_url)
        return new_url, new_id

    @staticmethod
    def __make_request(url):
        """
        Recieves an url and returns the raw html code of a webpage.
        :returns html: str
        :argument url: str
        """
        request = requests.get(url=url)  # , headers=headers
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
        div_review_blocks = soup.findAll('div', class_='fa-shadow movie-review-wrapper rw-item')
        return div_review_blocks

    @staticmethod
    def __filter_data(div_blocks):
        """
        Recibo lista de div y filtro las reviews en base a los ratings. return diccionario con 3 listas.
        :returns datos : dict
        :argument div_blocks: list
        """
        # malas: 1-4
        # neutras: 5-7
        # buenas: 8-10
        datos = {
            'malas': [],
            'neutras': [],
            'buenas': []
        }
        for block in div_blocks:
            soup = BeautifulSoup(str(block), 'html.parser')
            rating = soup.find('div', class_='user-reviews-movie-rating')  # {'class': 'user-reviews-movie-rating'}
            regex = r'<[^>]*>'
            rating = re.sub(regex, '', str(rating))
            rating = rating.replace(' ', '')
            rating = int(rating)
            review = soup.find('div', class_='review-text1')
            review = re.sub(regex, '', str(review))
            review = review.replace('\n', '')
            review = review.replace('\r', '')
            if rating == 1 or rating == 2 or rating == 3 or rating == 4:
                datos['malas'].append(review)
            elif rating == 5 or rating == 6 or rating == 7:
                datos['neutras'].append(review)
            elif rating == 8 or rating == 9 or rating == 10:
                datos['buenas'].append(review)
            else:
                print('no tengo rating')

        # print(datos)
        return datos

    def scrape(self, url):
        data = {
            'malas': [],
            'neutras': [],
            'buenas': []
        }

        print('empieza el scrape ' + url)
        num_page = 1
        max = 2
        new_url, id = self.change_urls(url)
        print('segundoURL ' + new_url)
        while num_page < max:
            url_aux = 'https://www.filmaffinity.com/es/reviews/' + str(num_page) + '/' + id
            html = self.__make_request(url_aux)
            blocks = self.__get_div_blocks(html)
            filtered_data = self.__filter_data(blocks)
            if len(filtered_data) is not 0:
                for malas in filtered_data['malas']:
                    data['malas'].append(malas)
                for neutras in filtered_data['neutras']:
                    data['neutras'].append(neutras)
                for buenas in filtered_data['buenas']:
                    data['buenas'].append(buenas)
                num_page += 1
            else:
                num_page = max
        return data


if __name__ == '__main__':
    sc = Filmaffinity()
    url = ['https://www.filmaffinity.com/es/film206403.html']
    data = sc.scrape(url[0])
    print(data)
