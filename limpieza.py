import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
en_stops = set(stopwords.words('spanish'))

all_words = ['Hola', 'es', 'un', 'caramelo','rico','el','coco']
for word in all_words: 
    if word not in en_stops:
        print(word)