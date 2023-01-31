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

# id=client.get_me().json()['data']['id']
# id=1427819523164368896
pprint.pprint(client.get_pinned_lists().json()['data'])
