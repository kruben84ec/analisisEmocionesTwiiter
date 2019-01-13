import setup as configuracion


tweeter = configuracion.ApiTweetpy()
api = tweeter.getApi()
# usuario de twitter
name = input("Ingresa al cuenta de tweeter que deseas sin @:")
# número de tweets
tweetCount = 10

resultado = api.user_timeline(id=name, count=tweetCount)

for tweet in resultado:
	print(tweeter.setText(tweet.text))

# import tweepy
# import csv
# import numpy
# import time
# import json


# class listener(StreamListener):
#  	"""docstring for ClassName"""
#  	def on_data(self, data):
#  		try:
#  			all_data = json.loads(data)
#  			tweet = all_data["text"]
#  			username = all_data["user"]["screen_name"]
#  			print((username, tweet))
#  			# blob = TextBlob(tweet)
#  			# print(blob.sentiment)
#  			#  print (data)
#  			# tweet = data.split(',"text":"')[1]
#  			# print (tweet)
#  			# saveThis = tweet+","+username
#  			# saveFile = open('twwiterDB4.csv', 'a')
#  			# saveFile.write(saveThis)
#  			# saveFile.write('/n')
#  			# saveFile.close()
#  			return True
#  		except BaseException:
#  			print('Ha fallado on_data', str(e))
#  			time.sleep(5)


#  	def on_error(self, status):
#  		print (status)

# auth = OAuthHandler(ckey, csecret)
# auth.set_access_token(atoken, asecret)
# twitterStream = Stream(auth, listener())
# searchTerm = input("Ingresa la cuenta o la tendencia que deseas  buscar en tweeter:")
# twitterStream.filter(track=[""+searchTerm])