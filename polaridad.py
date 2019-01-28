
from translate import Translator
from textblob import TextBlob

class Polaridad():

	def get_polaridad(self, text):
		frases = ""
		analizarTexto = ""
		frases = text
		analizarTexto = self.get_traductor(frases, "spanish", "english")

		polaridad = TextBlob(analizarTexto)
		print(polaridad.sentiment)
		return polaridad.sentiment

	def get_traductor(self, text, entrada, salida):
		translator = Translator(from_lang = entrada, to_lang = salida)
		traduccion = translator.translate(text)
		return traduccion.upper()
