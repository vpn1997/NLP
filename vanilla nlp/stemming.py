# stemming = getting root of the word

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
text=["fuck","fucker","fucked","fucking"]
sent="fuck has fucked every fucker in this fucking world in a fucking way motherfucker"
word=word_tokenize(sent)
for w in word:
    print ps.stem(w)
