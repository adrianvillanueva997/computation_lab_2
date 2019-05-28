from abc import ABC, abstractmethod

class Scrapper(ABC):
    @abstractmethod
    def __make_request(url):
        print("Implementar método")
    @abstractmethod
    def __get_divs(html):
        pass
    def __get_reviews(divs):
        pass