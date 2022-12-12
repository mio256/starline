import os
import datetime
import time
import requests
import tweepy
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
    access_token_secret,
    return_type=requests.Response
)

for users_tweets in tweepy.Paginator(
    client.get_home_timeline,
    max_results=100,
    start_time=datetime.datetime.now() - datetime.timedelta(days=1)
):
    for tweet in users_tweets.json()["data"]:
        id = tweet["id"]
        print(f'{id}')
        try:
            client.like(id)
        except tweepy.errors.BadRequest:
            print('done')
        except tweepy.errors.TooManyRequests:
            time.sleep(60)
