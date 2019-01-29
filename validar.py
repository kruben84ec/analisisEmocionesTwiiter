# import nltk.classify.util
# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import names
 
# def word_feats(words):
#     return dict([(word, True) for word in words])
 
# positive_vocab = [ 'bueno', 'atencion', 'victoria', 'campeon', 'idea', 'felicidad', 'gracias', ':)' ]
# negative_vocab = [ 'putos', 'terrible','pesimo', 'odio', 'desaprecer', 'supersisora', 'putas' ]

# positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
# negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]

 
# train_set = negative_features + positive_features 
 
# classifier = NaiveBayesClassifier.train(train_set) 
 
# # Predict
# neg = 0
# pos = 0
# sentence = "Servicio pesimo y por eso tenemos que desaprecer a la supervisora"
# sentence = sentence.lower()
# words = sentence.split(' ')
# for word in words:
#     classResult = classifier.classify( word_feats(word))
#     if classResult == 'neg':
#         neg = neg + 1
#     if classResult == 'pos':
#         pos = pos + 1
 
# print('Positive: ' + str(float(pos)/len(words)))
# print('Negative: ' + str(float(neg)/len(words)))

# import csv
# import polaridad as polaridadClase
# import setup as configuracion
# import matplotlib.pyplot as plt

# tweeter = configuracion.ApiTweetpy()
# analizarPolaridad = polaridadClase.Polaridad()


# class SentimentAnalisis():
# 	def getListCSV(self, archivo):
# 		# leyendo el archivo
# 		listaCsv = []
# 		with open(archivo, 'r') as f:
# 			reader = csv.reader(f)
# 			lista = list(reader)
# 		# extaryendo los datos del csv
# 		filas = len(lista)
# 		for x in range(filas):
# 			data = lista[x]
# 			if len(data) != 3:
# 				for lin in data:
# 					my_list = lin.split(";")
# 				if len(my_list) == 10:
# 					listaCsv.append(my_list)
# 		return listaCsv

# 	# function to calculate percentage
# 	def percentage(self, part, whole):
# 		temp = 100 * float(part) / float(whole)
# 		return format(temp, '.2f')



# analisisDatos = SentimentAnalisis()
# datosCsv = analisisDatos.getListCSV('BancoPichinchaFinal.csv')
#  # creating some variables to store info
# polarity = 0
# positive = 0
# negative = 0

# muestra = len(datosCsv)

# for i in range(20):
# 	text = datosCsv[i][6]
# 	polaridad = analizarPolaridad.get_polaridad(text)
# 	polarity += polaridad.polarity
# 	datosCsv[i][7] = polaridad.polarity
# 	print(text)
# 	print(datosCsv[i][7])
# 	# analizar la polaridad de la frase
# 	if polaridad.polarity > 0:
# 		positive += 1
# 	else: 
# 		negative += 1

# positive = analisisDatos.percentage(positive, muestra)
# negative = analisisDatos.percentage(negative, muestra)
# # finding average reaction
# polarity = polarity / muestra

# print("General Report: ")

# if (polarity == 0):
# 	print("Neutral")
# elif (polarity > 0 and polarity <= 0.3):
# 	print("Weakly Positive")
# elif (polarity > 0.3 and polarity <= 0.6):
# 	print("Positive")
# elif (polarity > 0.6 and polarity <= 1):
# 	print("Strongly Positive")
# elif (polarity > -0.3 and polarity <= 0):
# 	print("Weakly Negative")
# elif (polarity > -0.6 and polarity <= -0.3):
# 	print("Negative")
# elif (polarity > -1 and polarity <= -0.6):
# 	print("Strongly Negative")

# print()
# print("Detailed Report: ")
# print(str(positive) + "% people thought it was positive")
# print(str(negative) + "% people thought it was negative")


# for x in range(15):
#   data = your_list[x]
#   if len(data) != 3:
#       for lin in data:
#           my_list = lin.split(";")
#           if len(my_list) == 10:
#               if my_list[6] != '':
#                   frase = my_list[6]
#                   nueva = tweeter.setText(frase)
#                   polaridad = analizarPolaridad.get_polaridad(nueva)

#                   print(nueva)
#                   if polaridad.polarity > 0:
#                       print('positivo')
#                   elif polaridad.polarity == 0:
#                       print('neutral')
#                   else: 
#                       print('negativa')


