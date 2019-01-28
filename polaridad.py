#ejemplo de setimientos
from translate import Translator
from textblob import TextBlob
# translator = Translator(from_lang="spanish", to_lang="english")
# translation = translator.translate("AHORA SI  ESTADIO MONUMENTAL bancopichincha VA REGRESANDO NIVEL  SIEMPRE DEBIO TENER  HERMOSA NUESTRA")

# # print(translation.upper())
# frase = translation.upper()
# analysis = TextBlob(frase)
# print(analysis.sentiment)

class Polaridad():

	def get_polaridad(self, text):
		return text

	def get_traductor(self, text, configuracion):
		translator = Translator(from_lang=configuracion.entrada, to_lang= configuracion.out)
		traduccion = translator.translate(text)
		return traduccion.upper()
