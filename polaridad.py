
from translate import Translator
from textblob import TextBlob

class Polaridad():

	def get_polaridad(self, text):
		text = self.get_traductor(text, "spanish", "english")
		polaridad = TextBlob(text)
		return polaridad.sentiment

	def get_traductor(self, text, entrada, salida):
		translator = Translator(from_lang = entrada, to_lang = salida)
		traduccion = translator.translate(text)
		return traduccion.upper()
