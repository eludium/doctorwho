# irgend nen zeugs importieren
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

# oeffne Textdatei
f = open('test.txt', 'rU')

# lese Textdatei
raw = f.read()

# txt umwandeln damit nltk damit arbeiten kann
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

# nltk methode concordance aufrufen
text.concordance('test')
