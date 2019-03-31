import string

import pandas as pd
from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from Interfaces.Database.ETL.Modules import Models

df = pd.read_csv('spamraw.csv')

x = df['text']
y = df['type']

print(x, y)


def tokenizer(reviews):
    """
    Tokenizing, stemming and stop words filtering process
    :param reviews:
    :return : list
    """
    stems = []
    stop_words = set(stopwords.words('english'))
    token = word_tokenize(text=reviews, language='english')
    for item in token:
        if item not in stop_words and item not in string.punctuation:
            stems.append(SnowballStemmer(language='english').stem(item))

    return stems


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

models = Models.Models(x_train, x_test, y_train, y_test)

text_clf = Pipeline([('vect', CountVectorizer(tokenizer=tokenizer, lowercase=True, encoding='utf-8')),
                     ('tfidf', TfidfTransformer()), ])
# ('clf', GaussianNB()), ])

a = text_clf.fit_transform(x_train, y_train)
a = a.toarray
print(a)
