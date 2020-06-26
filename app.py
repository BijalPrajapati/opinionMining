import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

'''for tweet in tweepy.Cursor(api.search,q="#iPhone11Pro",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)'''
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

tweets = tweepy.Cursor(api.search,
                       q="#iPhone11Pro",
                       lang="en",
                       since="2017-04-03").items()

#print(tweets)
users_locs = [[tweet.user.screen_name, tweet.user.location,tweet.created_at, tweet.text.encode('utf-8')] for tweet in tweets]
#csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
print(users_locs)
