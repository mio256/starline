import os
from requests_oauthlib import OAuth1Session


def url_split_dict(url):
    splited_url = url.split("&")
    return {x.split("=")[0]: x.split("=")[1] for x in splited_url}


def login():
    API_KEY = os.environ['CONSUMER_KEY']
    API_KEY_SECRET = os.environ['CONSUMER_SECRET']

    callback_url = "http://127.0.0.1:8000/oauth/"
    request_endpoint_url = "https://api.twitter.com/oauth/request_token"
    authenticate_url = "https://api.twitter.com/oauth/authenticate"

    session_req = OAuth1Session(API_KEY, API_KEY_SECRET)
    response_req = session_req.post(request_endpoint_url, params={"oauth_callback": callback_url})
    response_req_text = response_req.text

    token_dict = url_split_dict(response_req_text)
    oauth_token = token_dict["oauth_token"]

    print(f'{authenticate_url}?oauth_token={oauth_token}')


def oauth(url):
    oauth_token_dict = url_split_dict(url.split("?")[1])
    oauth_token = oauth_token_dict['oauth_token']
    oauth_verifier = oauth_token_dict['oauth_verifier']
    access_endpoint_url = "https://api.twitter.com/oauth/access_token"

    API_KEY = os.environ['CONSUMER_KEY']
    API_KEY_SECRET = os.environ['CONSUMER_SECRET']

    session_acc = OAuth1Session(API_KEY, API_KEY_SECRET, oauth_token, oauth_verifier)
    response_acc = session_acc.post(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
    response_acc_text = response_acc.text

    acc_token_dict = url_split_dict(response_acc_text)
    access_token = acc_token_dict["oauth_token"]
    access_token_secret = acc_token_dict["oauth_token_secret"]

    return access_token, access_token_secret
