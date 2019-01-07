import csv, re
import time, json, numpy
#setup tweeter
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from credenciales import * # agregamos las credenciales


class SetupTweetPy:
	def __init__(self):
		self.tweets = []
		self.tweetText = []

	def cleanTweet(self, tweet):
 		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

	def getData(self):
		# auth = tweepy.OAuthHandler(ckey, csecret)
		# auth.set_access_token(atoken, asecret)
		# api = tweepy.API(auth)
		searchTerms = input("Tweet a buscar:")
		# numTerms = int(input("Número de tweets:"))
		# self.tweets = tweepy.Cursor(api.search, q = searchTerms, lang = "es" ).items(numTerms)

		# for tweet in self.tweets:
		# 	tweetText = tweet.text
		# 	username = tweet.user.screen_name
		# 	rowTweet = username+":"+tweetText+""
		# 	self.tweetText.append(rowTweet)

		archivo = "base_"+searchTerms+"_"



sa = SetupTweetPy()
sa.getData()