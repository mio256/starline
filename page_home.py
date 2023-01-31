import os
import datetime
import requests
import pprint
import tweepy

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response
)


for users_tweets in tweepy.Paginator(
    client.get_home_timeline,
    exclude=['retweets', 'replies'],
    tweet_fields=['public_metrics'],
    max_results=100,
    start_time=datetime.datetime.now() - datetime.timedelta(days=1)
):
    pprint.pprint(users_tweets.json()["data"])
