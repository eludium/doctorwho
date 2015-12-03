# irgend nen zeugs importieren
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

# öffne Textdatei
f = open('all_words_12th_doctor.txt', 'rU')

# die decodierung geht aber irgendwie nicht, wenn man ne .txt nimmt mit "bla bla bla" geht alles
# aber sobald Üä*+ oder sonstige Sachen dabei sind, kackt et ab
raw = f.read().decode('utf8')

# txt umwandeln damit nltk damit arbeiten kann
tokens = nltk.word_tokenize(raw).txt
text = nltk.Text(tokens)

# nltk methode concordance aufrufen
text.concordance('doctor')
