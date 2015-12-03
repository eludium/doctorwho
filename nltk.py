# irgend nen zeugs importieren
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import codecs

# oeffne Textdatei
f = codecs.open('12_doctor_all_words.txt', 'rU', 'UTF-8-sig')

# die decodierung geht aber irgendwie nicht, wenn man ne .txt nimmt mit "bla bla bla" geht alles
# aber sobald oder sonstige Sachen dabei sind, kackt et ab (auch wenn hier in den Kommentaren Umlaute sind... meh)
raw = f.read()

# txt umwandeln damit nltk damit arbeiten kann
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

# nltk methode concordance aufrufen
associations = text.concordance('die')
