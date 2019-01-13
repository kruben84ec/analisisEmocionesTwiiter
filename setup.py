#setup tweeter
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from credenciales import * # agregamos las credenciales

class ApiTweetpy():
	"""docstring for getApiTweetpy"""
	def getApi(self):
		auth = tweepy.OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		return tweepy.API(auth)