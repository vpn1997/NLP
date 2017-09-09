from gensim.models import Word2Vec
from nltk.corpus import brown,movie_reviews,treebank

b=Word2Vec(brown.sents())
mr=Word2Vec(movie_reviews.sents())
t=Word2Vec(treebank.sents())

print b.most_similar('money',topn=5)