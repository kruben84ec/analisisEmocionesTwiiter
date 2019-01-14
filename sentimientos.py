#ejemplo de setimientos
# from translate import Translator
from textblob import TextBlob
analysis = TextBlob("Bad")
print(analysis.sentiment)
# print(analysis.tags)
# print(analysis.translate(to='es'))
# print(dir(analysis))