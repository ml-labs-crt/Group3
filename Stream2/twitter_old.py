import sys
import getopt
import csv
from datetime import datetime

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

tweetCriteria = got.manager.TweetCriteria().setSince("2019-10-10").setUntil("2018-10-10").setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
print(tweet.text)