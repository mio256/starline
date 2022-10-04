import os
import tweepy

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET'],
    wait_on_rate_limit=True
    )

client.create_tweet(text='hello')
