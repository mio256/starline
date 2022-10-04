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

data={}

min_ret = input('min_retweet>')

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
            if tweet.public_metrics['retweet_count'] > int(min_ret):
                data[tweet.id]=ret
except Exception as e:
    print(e)

data_sorted = sorted(data.items(), key=lambda x:-x[1])

for tweet in data_sorted:
    print('retweet:{} https://twitter.com/redirect/status/{}'.format(tweet[1],tweet[0]))

    response = client.get_tweet(tweet[0], expansions=['author_id'])
    name=response.includes['users'][0]['name']
    text=response.data.text
    print(name)
    print(text)

    input()

