

#This script allows to extract all the Tweets with a given query published.
#Tweeter only allows to extract tweets beyond 7 days
#there is a limit of 180 queries per 15 minutes

#Tweepy must be installed in advanced
#You need to modify your credentials (access token, accesss token secret, consumer key and consumer secret), the query and the starting and ending dates

#author: sandra acebes (https://github.com/Sacebes)
#last update : Jan 7,2019

import csv
import sys
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API (modify with your own credentials) 
access_token = "XXXXX"
access_token_secret = "XXXXX"
consumer_key = "XXXXX"
consumer_secret = "XXXXX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


csvFile = open('./output_twitter.csv', 'a')
csvWriter = csv.writer(csvFile)
fileout = open("./output_twitter.txt",'w')


#search parameters (modify)
query = "happy new year" #Write here the keyword you want to search
language = "en" #Modify if you are interested in other languages, for example, spanish = "es"
starting_date = "2018-12-31"  #Write here the starting date aa-mm-dd
ending_date = "2019-01-02"    #Write here the last day aa-mm-dd

for tweet in tweepy.Cursor(api.search,q=query,lang=language,tweet_mode="extended", since=starting_date,until=ending_date).items():
        fileout.write(str(tweet))  #print the whole tweet in json format
        csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')]) #print only date and text

csvFile.close()
fileout.close()

