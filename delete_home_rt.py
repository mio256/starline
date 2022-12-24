import os
import pprint
import requests
import tweepy
import readchar

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=requests.Response,
    wait_on_rate_limit=True
)

pprint.pprint(client.get_me().json())

ids = []

for users_tweets in tweepy.Paginator(
    client.get_users_tweets,
    id=client.get_me().json()['data']['id'],
    exclude=['retweets', 'replies'],
    tweet_fields=['public_metrics'],
    max_results=100
):
    for tweet in users_tweets.json()['data']:
        print(tweet['text'])
        print(f'retweet:{tweet["public_metrics"]["retweet_count"]+tweet["public_metrics"]["quote_count"]}',
              f'like:{tweet["public_metrics"]["like_count"]}',
              f'reply:{tweet["public_metrics"]["reply_count"]}')
        if int(tweet["public_metrics"]["retweet_count"])+int(tweet["public_metrics"]["quote_count"])<5:
            c = readchar.readkey()
            if c == 'd':
                client.delete_tweet(tweet['id'])
