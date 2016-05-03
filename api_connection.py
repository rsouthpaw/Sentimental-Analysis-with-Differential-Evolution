#This file contain a third party library
#Download Twitter library from pip install twitter command
#Various other libraries also work like tweepy

import twitter
CONSUMER_KEY = key
CONSUMER_SECRET = secret1
OAUTH_TOKEN = access
OAUTH_TOKEN_SECRET = secret2
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print twitter_api

#mail id: saranshmiglani@gmail.com