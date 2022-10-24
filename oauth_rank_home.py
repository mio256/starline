import os
import tweepy
import datetime
import webbrowser
from oauth import oauth, login


def id_to_username(id: str):
    response = client.get_user(id=id)
    return response.data.username


login()
url = input('url>')
access_token, access_token_secret = oauth(url)
print(access_token, access_token_secret)

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    access_token,
    access_token_secret
)

data = {}

days = int(input('days>'))
retweets = int(input('retweets>'))

try:
    for tweets in tweepy.Paginator(
        client.get_home_timeline,
        exclude=['retweets', 'replies'],
        tweet_fields=['public_metrics'],
        max_results=100,
        start_time=datetime.datetime.now() - datetime.timedelta(days=days)
    ):
        print(tweets.meta)
        for tweet in tweets.data:
            ret = tweet.public_metrics['retweet_count']
            if tweet.public_metrics['retweet_count'] > retweets:
                data[tweet.id] = ret
except Exception as e:
    print(e)

data_sorted = sorted(data.items(), key=lambda x: x[1])

for tweet in data_sorted:
    url = f'https://twitter.com/redirect/status/{tweet[0]}'
    print(f'retweet:{tweet[1]}')
    webbrowser.open(url, new=0, autoraise=True)
