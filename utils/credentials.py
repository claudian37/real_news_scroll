from os import environ

twitter_auth_keys = {
    "consumer_key": environ['twitter_consumer_key'],
    "consumer_secret": environ['twitter_consumer_secret'], 
    "access_token": environ['twitter_access_token'],
    "access_token_secret": environ['twitter_access_token_secret']
}

bitly_auth_keys = {
    "username": environ['bitly_username'],
    "password": environ['bitly_password'],
    "auth_token": environ['bitly_auth_token']
}