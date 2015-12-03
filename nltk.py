# irgend nen zeugs importieren
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

# oeffne Textdatei
f = open('test.txt', 'rU')

# die decodierung geht aber irgendwie nicht, wenn man ne .txt nimmt mit "bla bla bla" geht alles
# aber sobald oder sonstige Sachen dabei sind, kackt et ab (auch wenn hier in den Kommentaren Umlaute sind... meh)
raw = f.read()

# txt umwandeln damit nltk damit arbeiten kann
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

# nltk methode concordance aufrufen
text.concordance('test')
