#setup tweeter
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from credenciales import * # agregamos las credenciales


class SetupTweetPy:
	"""docstring for DowloadData"""
	def __init__(self):
		self.tweets = []
		self.tweetTex = []

	def getData(self):
		auth = tweepy.OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		return tweepy.API(auth)

