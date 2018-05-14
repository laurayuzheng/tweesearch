import json
from bs4 import BeautifulSoup
import re
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets
from textblob import TextBlob
from textblob import Word

 
import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from subprocess import check_output

data = pd.read_json('my_dict.json')
nouns = list()
def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
def analize_sentiment(tweet):
    
    analysis = TextBlob(tweet)
    for word, tag in analysis.tags:
    	if tag == 'NN':
    		nouns.append(word)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
cleaned = []
for key,value in data.items():
	val = str(BeautifulSoup(value[0], 'html5lib'))
	val=val.replace('body', '')
	val=val.replace('head', '')
	val=val.replace('html', '')
	val = clean_tweet(val)

	cleaned.append(val)
stopwords = set(STOPWORDS)

data_sent = np.zeros((2,len(cleaned)))
data_sent[0]=np.array([ analize_sentiment(val) for val in cleaned ])
wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=50000,
                          max_font_size=40, 
                          random_state=42
                         ).generate(', '.join(nouns))
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=900)

