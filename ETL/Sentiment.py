from polyglot.detect import Detector
from googletrans import Translator


class Sentiment:
    def __init__(self):
        self.__text_list = []

    @staticmethod
    def __text_to_english(text):
        eng_text = Translator().translate(text)
        return eng_text

    def analyse_texts(self, texts):
        translated_texts = []
        for text in texts:
            translated_text = self.__text_to_english(text)
            print(translated_text.text)
            translated_texts.append(translated_text.text)

    def analyse_sentence(self, sentence):
        translated_text = self.__text_to_english(sentence)
        print(translated_text.text)
        

if __name__ == '__main__':
    texts = ['Hola me llamo Adrián']
    sentiment = Sentiment()
    sentiment.analyse_texts(texts=texts)
