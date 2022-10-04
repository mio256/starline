import os
import tweepy
import datetime
import pprint

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
)

def id_to_username(id: str):
    response = client.get_user(id=id)
    return response.data.username

data={}

try:
    for tweets in tweepy.Paginator(
        client.get_home_timeline,
        exclude=['retweets', 'replies'],
        tweet_fields=['public_metrics'],
        max_results=100,
        start_time=datetime.datetime.now() - datetime.timedelta(days=1)
    ):
        print(tweets.meta)
        for tweet in tweets.data:
            ret = tweet.public_metrics['retweet_count']
            if tweet.public_metrics['retweet_count'] > 10:
                data[tweet.id]=ret
except Exception as e:
    print(e)

data_sorted = sorted(data.items(), key=lambda x:x[1])

for tweet in data_sorted:
    print('retweet:{} https://twitter.com/redirect/status/{}'.format(tweet[1],tweet[0]))