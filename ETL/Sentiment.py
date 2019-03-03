from googletrans import Translator
from textblob import TextBlob
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
        time.sleep(2)
        eng_text = Translator().translate(text)
        return eng_text

    @staticmethod
    def __text_to_english_backup(text):

        time.sleep(2)
        blob = TextBlob(text)
        language_code = blob.detect_language()
        print(language_code)
        if language_code is 'en':
            return text
        else:
            english_text = blob.translate(to='en')
            print(language_code)
            print(english_text)
            return english_text

    def analyse_texts(self, texts):
        """
        Public method that receives a list of texts and translates them into english
        and analyses its sentiment and polarity.
        :param texts:
        """
        sentiments = {
            'texts': texts,
            'polarity': [],
            'subjectivity': [],
            'positivity': [],
            'negativity': [],
            'neutrality': [],
            'compound': []
        }
        for text in texts:
            translated_text = None

            try:
                translated_text = self.__text_to_english(text)
            except Exception as e:
                translated_text = self.__text_to_english_backup(text)
            if translated_text is not None:
                try:
                    english_text = translated_text.text
                except Exception as e:
                    print(e)
                    english_text = translated_text
                polarity, subjectivity = self.__blob_sentiment_analysis(english_text)
                sentiments['polarity'].append(polarity)
                sentiments['subjectivity'].append(subjectivity)
                neg, neu, pos, comp = self.__vader_sentiment_analysis(english_text)
                sentiments['negativity'].append(neg)
                sentiments['neutrality'].append(neu)
                sentiments['positivity'].append(pos)
                sentiments['compound'].append(comp)
        self.__sentiments = sentiments
        print(self.__sentiments)
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
        translated_text = None
        try:
            translated_text = self.__text_to_english(sentence)
        except Exception as e:
            translated_text = self.__text_to_english_backup(sentence)
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
