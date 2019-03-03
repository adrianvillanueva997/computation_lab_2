from googletrans import Translator
from textblob import TextBlob
import translate
from polyglot.detect import Detector
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import time


class Sentiment:
    def __init__(self):
        """
        Default constructor
        """
        self.__text_list = []
        self.__sentiments = {}

    @staticmethod
    def __text_to_english(text):
        """
        Function that detects a language and returns it translation in english
        :param text:
        :return:
        """
        try:
            time.sleep(2)
            eng_text = Translator().translate(text)
            return eng_text
        except Exception as e:
            print(e)

    def analyse_texts(self, texts):
        """
        Public method that receives a list of texts and translates them into english
        and analyses its sentiment and polarity.
        :param texts:
        """
        sentiments = {
            'texts': [],
            'polarity': [],
            'subjectivity': [],
            'positivity': [],
            'negativity': [],
            'neutrality': [],
            'compound': []
        }
        for text in texts:
            translated_text = self.__text_to_english(text)
            if translated_text is not None:
                english_text = translated_text.text
                print(english_text)
                polarity, subjectivity = self.__blob_sentiment_analysis(english_text)
                sentiments['polarity'].append(polarity)
                sentiments['subjectivity'].append(subjectivity)
                neg, neu, pos, comp = self.__vader_sentiment_analysis(english_text)
                sentiments['negativity'].append(neg)
                sentiments['neutrality'].append(neu)
                sentiments['positivity'].append(pos)
                sentiments['compound'].append(comp)
            self.__sentiments = sentiments
            return sentiments

    def analyse_sentence(self, sentence):
        """
        Public method that translates a single sentence into english and returns its sentiment
        analysis and polarity
        :param sentence:
        """
        sentiments = {
            'polarity': [],
            'subjectivity': [],
            'positivity': [],
            'negativity': [],
            'neutrality': [],
            'compound': []
        }
        translated_text = self.__text_to_english(sentence)
        if translated_text is not None:
            english_text = translated_text.text
            polarity, subjectivity = self.__blob_sentiment_analysis(english_text)
            sentiments['polarity'].append(polarity)
            sentiments['subjectivity'].append(subjectivity)
            neg, neu, pos, comp = self.__vader_sentiment_analysis(english_text)
            sentiments['negativity'].append(neg)
            sentiments['neutrality'].append(neu)
            sentiments['positivity'].append(pos)
            sentiments['compound'].append(comp)
            self.__sentiments = sentiments
            return sentiments

    @staticmethod
    def __blob_sentiment_analysis(text):
        """
        Sentiment analysis using TextBlob library
        :param text:
        :return:
        """
        blob = TextBlob(text)
        sent = blob.sentiment
        polarity = sent.polarity
        subjectivity = sent.subjectivity
        return polarity, subjectivity

    @staticmethod
    def __vader_sentiment_analysis(text):
        """
        Text analysis using vader, returns all sentiment values
        :param text:
        :return:
        """
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(text)
        return ss['neg'], ss['neu'], ss['pos'], ss['compound']

    def export_sentiment_to_csv(self, path, file_name):
        """
        Exports the sentiments obtained by previous functions
        :param path:
        :param file_name:
        :return:
        """
        df = pd.DataFrame(data=self.__sentiments)
        df.to_csv(f'{path}{file_name}.csv', index=None)
