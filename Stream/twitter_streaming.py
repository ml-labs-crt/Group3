# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '556088690-mNC0w7siuT1xpC2ejdcG6vCw7ZUPsHEY86oMvcpT'
ACCESS_SECRET = '4jmrhzpTvGhXG031PgD11XRMBrqP80hQEghi8gZScuqsa'
CONSUMER_KEY = 'j1FeBFunpuWSWvedKukC0WJg2'
CONSUMER_SECRET = 'CefIY8Zi1FODzKF4xTpplNdd8WcVbl5piMzdqA3W1QgZ0Wzbjt'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

#for status in tweepy.Cursor(api.home_timeline).items(200):
#	print(status._json)
	
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# Attempt to receive twitts by location.
# geocode ----> [latitude,longitude,radius] --- [37.781157,-122.398720,1km]
#---------------------------------------------------------------------------------------------------------------------
for tweet in tweepy.Cursor(api.search,q="*",count=100,geocode="41.385100,2.173400,15km",languages=["es"]).items(100):
    print(tweet.text)
    print(tweet.geo)
    print(tweet.created_at)
    
