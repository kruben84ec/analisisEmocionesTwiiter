#ejemplo de setimientos
from translate import Translator
from textblob import TextBlob
translator= Translator(from_lang="spanish", to_lang="english")
translation = translator.translate("Enfrentemos el odio la discriminación y el machismo el compromiso es de todos")
print(translation.upper())
frase = translation.upper()
analysis = TextBlob(frase)
print(analysis.sentiment)

