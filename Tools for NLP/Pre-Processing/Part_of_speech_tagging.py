import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
#Punktsentoken is firstly maually trained then it is used to toeknize sentences
train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=  PunktSentenceTokenizer(train_text) #train
tokenized=custom_sent_tokenizer.tokenize(sample_text)   #test

for i in tokenized:
    words=nltk.word_tokenize(i)
    print nltk.pos_tag(words)

