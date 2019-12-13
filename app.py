import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'OWefnzVZag8ocIflOS2XU2ZFb'
consumer_secret = '1brbJunSiIX7pxDBQsbYq1a1GicaTWRICLkGiOMKXda73Cv6UU'
access_token = '1195050243215245314-EUXEkijjyp0jeoJUUy1B9jjrDoUvHj'
access_token_secret = 'j4OCrcobvTZR117s4Ug6jbpieiaIz83r1Oj5aKHA4ZEnW'



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