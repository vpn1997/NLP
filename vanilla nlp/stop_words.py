from  nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text="Girls aint no hoe but this is just a corpus."
stop_word=set(stopwords.words("english"))
text_tokenize=word_tokenize(text)
filter_words=[]
for word in text_tokenize  :
    if word not in stop_word:
        filter_words.append(word);
print filter_words;