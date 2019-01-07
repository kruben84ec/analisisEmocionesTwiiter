#setup tweeter
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from credenciales import * # agregamos las credenciales


class listener(StreamListener):
 	"""docstring for ClassName"""
 	def on_data(self, data):
 		print (data)
 		return True
 	def on_error(self, status):
 		print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = setupTweeter.Stream(auth, listener())
twitterStream.filter(track=["car"])