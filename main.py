import setup as configuracion
import json
#REFENCIA https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
#https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/premium-operators
tweeter = configuracion.ApiTweetpy()
api = tweeter.getApi()

while True:
	try:
		print("---------------------------------------------------------")
		name = input("Ingresa al cuenta de tweeter que deseas sin @:")
		# user = api.get_user(name)
		# print(user.followers_count)
		# for friend in user.friends():
		# 	print(friend.screen_name)
		# # número de tweets
		tweetCount = int(input("Número de tweets"))
		resultado = api.user_timeline(id=name, count=tweetCount, full_text=True)

		for tweet in resultado:
			print(tweet.created_at)
			print(tweeter.setText(tweet.user.location))
			print(tweeter.setText(tweet.user.screen_name))
			print(tweeter.setText(tweet.text))

		print("---------------------------------------------------------")
	except Exception as e:
		print('Ha fallado:', str(e))

	continuar = input("¿Desea Continuar <S=si/N=no>?")

	if(continuar[0].upper() == "N"):
		break




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