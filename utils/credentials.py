import os
from os import environ

twitter_auth_keys = {
    "consumer_key": os.getenv('twitter_consumer_key', ''),
    "consumer_secret": os.getenv('twitter_consumer_secret', ''),
    "access_token": os.getenv('twitter_access_token', ''),
    "access_token_secret": os.getenv('twitter_access_token_secret', '')
}

bitly_auth_keys = {
    "username": os.getenv('bitly_username', ''),
    "password": os.getenv('bitly_password', ''),
    "auth_token": os.getenv('bitly_auth_token', '')
}