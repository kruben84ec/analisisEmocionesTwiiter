import setup as configuracion
import json
import csv
import pandas as pd
import tweepy
#REFENCIA https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
#https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/premium-operators
#https://gist.github.com/yanofsky/5436496
#https://github.com/Jefferson-Henrique/GetOldTweets-python
tweeter = configuracion.ApiTweetpy()
api = tweeter.getApi()
results = []
for tweet in tweepy.Cursor(api.search, 
	q="BancoPichincha -BARCELONASC -UCATOLICAGYE",
	include_entities=True,
	wait_on_rate_limit=True,
	since="2018-12-12", 
	until="2019-12-12", 
	wait_on_rate_limit_notify=True,
	lang="es",
	src="typd").items(100):
	results.append(tweet)
#https://twitter.com/search?l=es&q=BancoPichincha%20-Barcelona%20since%3A2018-12-12%20until%3A2019-01-20&src=typd&lang=es
for tweet in results:
	print("(" + str(tweet.created_at) + ": " +tweeter.setText(tweet.text) + ")")



# while True:
# 	try:
# 		print("---------------------------------------------------------")
# 		name = input("Ingresa al cuenta de tweeter que deseas sin @:")
# 		tweetCount = int(input("Numero de tweets: "))
# 		resultado = api.user_timeline(id=name, count=tweetCount, full_text=True)
# 		for tweet in resultado:
# 			print(tweet.retweet_count)
# 			print(tweet.lang)
# 			print(tweet.created_at)
# 			print(tweet.id_str)
# 			print(tweeter.setText(tweet.user.location))
# 			print(tweeter.setText(tweet.user.name))
# 			print(tweeter.setText(tweet.user.screen_name))
# 			print(tweeter.setText(tweet.text))

# 		print("---------------------------------------------------------")
# 	except Exception as e:
# 		print('Ha fallado:', str(e))
# 	continuar = input("¿Desea Continuar <S=si/N=no>?")
# 	if(continuar[0].upper() == "N"):
# 		break




