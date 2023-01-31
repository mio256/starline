import os
import datetime
import pprint
import requests
import tweepy
import webbrowser
from oauth import oauth, login

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response
)

id_mi0256=1427819523164368896

for tweets in tweepy.Paginator(
    client.get_users_tweets,
    id=id_mi0256
):
    for tweet in tweets.json()['data']:
        pprint.pprint(tweet)
        client.like(tweet['id'])
        client.retweet(tweet['id'])
