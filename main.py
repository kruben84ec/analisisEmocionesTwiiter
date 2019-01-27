import setup as configuracion
import limpieza as clean
import tweepy

limpiar = clean.Clean_Tweet()
tweeter = configuracion.ApiTweetpy()
api = tweeter.getApi()
results = []

tweetDataSet = [];
for tweet in tweepy.Cursor(api.search, 
	q="BancoPichincha -BARCELONASC -UCATOLICAGYE",
	include_entities=True,
	wait_on_rate_limit=True,
	since="2018-12-15", 
	until="2019-01-27", 
	wait_on_rate_limit_notify=True,
	lang="es",
	src="typd",
	tweet_mode="extended").items(1):
	results.append(tweet)
	
for tweet in results:
	textTweet = tweeter.setText(tweet.full_text)
	tweetLimpio = limpiar.get_textClean(textTweet).upper()
	fechaCreacion = str(tweet.created_at)
	autor = tweeter.setText(tweet.author.name)
	seguidores = str(tweet.author.followers_count)
	idTweeter = tweet.id_str
	reTweet = str(tweet.retweet_count)
	idioma = tweet.lang
	geolocation = tweeter.setText(tweet.user.location)
	cuentaTweet = tweeter.setText(tweet.user.screen_name)
	tweetRegistro = [
		 idTweeter, 
		 fechaCreacion, 
		 autor,
		 geolocation,
		 cuentaTweet,
		 seguidores,
		 reTweet,
		 textTweet,
		 tweetLimpio,
		 geolocation

	]
	tweetDataSet.append(tweetRegistro)

print(tweetDataSet)



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




