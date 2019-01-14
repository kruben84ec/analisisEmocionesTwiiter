#ejemplo de setimientos
from translate import Translator
from textblob import TextBlob
translator= Translator(from_lang="spanish", to_lang="english")
translation = translator.translate("mas vale pajaro en mano que siento volando")
print(translation.upper())
frase = translation.upper()
analysis = TextBlob(frase)
print(analysis.sentiment)

