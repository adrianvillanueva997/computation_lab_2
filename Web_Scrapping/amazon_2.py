import requests


class Amazon:
    def __init__(self):
        pass

    def make_request(self, url):
        re = requests.get(url)
        html = re.content
        return html


if __name__ == '__main__':
    url = 'https://www.amazon.es/New-Super-Mario-Bros-Deluxe/product-reviews/B07HD1312V/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'
