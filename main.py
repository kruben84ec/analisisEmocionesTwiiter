import setup as configuracion
import limpieza as clean
import polaridad as polaridadClase
import csvGenerate as csvTool
import tweepy
import time

csvGenerar = csvTool.CSV_py()
analizarPolaridad = polaridadClase.Polaridad()
limpiar = clean.Clean_Tweet()
tweeter = configuracion.ApiTweetpy()
api = tweeter.getApi()
results = []

tweetDataSet = [];
#titulos
tweetHead = [
	"idTweeter",
	"fecha",
	"autor",
	"cuenta",
	"seguidores",
	"retweet",
	"textoLimpio",
	"polaridad",
	"subjetivo",
	"geolocalizacion"
	]

fechaArchivo = str(time.strftime("%Y%m%d"))


while True:
	try:
		print("---------------------------------------------------------")
		name = input("Ingresa al cuenta de tweeter que deseas sin @:")
		tweetCount = int(input("Numero de tweets: "))
		print("Empezo: "+str(time.strftime("%H:%M:%S")))
		for tweet in tweepy.Cursor(api.search, 
			q=" "+name+" -BARCELONASC -UCATOLICAGYE",
			include_entities=True,
			wait_on_rate_limit=True,
			since="2018-12-15", 
			until="2019-01-28", 
			wait_on_rate_limit_notify=True,
			lang="es",
			src="typd",
			tweet_mode="extended").items(tweetCount):
			results.append(tweet)
			
		for tweet in results:
			textTweet = tweeter.setText(tweet.full_text)
			tweetLimpio = limpiar.get_textClean(textTweet).upper()
			polaridadTweet = analizarPolaridad.get_polaridad(tweetLimpio)
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
				 cuentaTweet,
				 seguidores,
				 reTweet,
				 tweetLimpio,
				 polaridadTweet.polarity,
				 polaridadTweet.subjectivity,
				 geolocation
			]
			tweetDataSet.append(tweetRegistro)

		nombreArchivo = name+"_"+fechaArchivo
		csvGenerar.generar_csv(nombreArchivo, tweetHead, tweetDataSet)	
		print("Termino: "+str(time.strftime("%H:%M:%S")))	
		print("---------------------------------------------------------")
	except Exception as e:
		print('Ha fallado:', str(e))
	continuar = input("¿Desea Continuar <S=si/N=no>?")
	if(continuar[0].upper() == "N"):
		break




