import os
import tweepy

client = tweepy.Client(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ[ 'CONSUMER_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)


response = client.get_home_timeline()

for tweets in response:
    for tweet in tweets:
        print(tweet)
