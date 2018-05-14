import tweepy 
import json
import datetime          
import numpy as np      
from bs4 import BeautifulSoup as BS
from keys import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
tweets = api.home_timeline()
counter=0
dict_tweets={}
for tweet in tweepy.Cursor(api.search,q="geocode:38.9858884,-76.9424005,2km since:2018-05-01",lang = 'en').items():
    try:
    	dict_tweets[counter]=(tweet.text,tweet.created_at)
    	counter=counter+1
    except tweepy.TweepError as e:
        print(e.reason)
        continue
    except StopIteration:
        break
with open('my_dict.json', 'w') as f:
    json.dump(dict_tweets, f,default=datetime_handler)