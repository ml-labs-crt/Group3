# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import csv
import numpy as np

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
# wait_on_rate_limit_notify= True;  will make the api to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------
# CSV Management
# 
#---------------------------------------------------------------------------------------------------------------------
csvFile = open('Datasets/tweets4.csv', 'a')
csvWriter = csv.writer(csvFile)

#---------------------------------------------------------------------------------------------------------------------
# Receive twitts by location.
# geocode ----> [latitude,longitude,radius] --- [37.781157,-122.398720,1km]
#---------------------------------------------------------------------------------------------------------------------
count = 0
done = 0
for tweet in tweepy.Cursor(api.search,q="*",count=100,geocode="53.058004,-8.110000,200km",languages=["en"]).items(2500000):
    done = done + 1
    tweetOK = 0

    with open("keywords.txt", "r") as text: 
        keywords = [] 
        for line in text:
            line = line.split("\n")[0]
            keywords.append(line)
            keywords.append(line.lower())
            keywords.append(line.upper())
    
    ##########
    ## TEXT ##
    ##########
    text = tweet.text.encode('utf-8')
    text = str(text).split("'")[1]
    ##########
    ## Date ##
    ##########
    date = tweet.created_at
    ##############
    ## Location ##
    ##############
    if "coordinates" in str(tweet.geo):
        location = tweet.geo
        location = (str(location).split(':'))[2]
        location = location.split('[')[1]
        location = location.split(']')[0]
    else:
        location = '--'

    #Iteration of keywords
    for word in keywords:
        #If keyword found enable saving
        if text.find(word) != -1:
            tweetOK = 1
    #Saving
    if tweetOK == 1:
        #If it is not a RT
        if text[0:2] != 'RT':
            csvWriter.writerow([date, text, location])
            count = count +1
    print(done)
    print(count)