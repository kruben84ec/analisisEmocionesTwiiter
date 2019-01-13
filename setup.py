#setup tweeter
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import unicodedata
from credenciales import * # agregamos las credenciales

class ApiTweetpy():
	"""docstring for getApiTweetpy"""
	def __init__(self):
		self.tweetText = []

	def getApi(self):
		auth = tweepy.OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		return tweepy.API(auth)

	def limpiarCarateres(self, cadena):
		text = unicodedata.normalize("NFKD", cadena.decode("utf-8"))
		text = text.encode("ascii","ignore").decode("ascii")
		return text.upper()

	def setText(self, text): 
		text = self.encodeTex(text)
		return self.limpiarCarateres(text)

	def encodeTex(self, text):
		return text.encode('utf-8').upper()

	def getText(self, publicTweets):
		for tweet in publicTweets:
			text = self.setText(tweet.text)
			self.tweetText.append(text)
		return self.tweetText

	def getHomeTweeterText(self):
		apiTweeter = self.getApi()
		publicTweets = apiTweeter.home_timeline()
		return self.getText(publicTweets)
