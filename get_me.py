import os
import tweepy
import pprint
import requests

client = tweepy.Client(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ[ 'CONSUMER_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response
)

pprint.pprint(client.get_me().json()['data']['id'])
