# What is it?

Its a sentiment analysis program which helps in classfying the sentiment of live streamming tweets.
It can help in determine peoples opinion toward a product,service or person using their tweets through Twitter Streaming API.

# How it is built ?
 
 Meat of the program is in building the sentiment module , which can classify a given text in binary(pos or neg with some conf
 -idence value).To Build a corpus for training and testing i have  used positive.txt and negative.txt.Using both the files i built
 a Bag of word model using top 5000 most freq words(and some pos tagging).These 5000 words will now act as our word features.
 Text is classifed on the bases of the availabilty of these word features.
 
 Now for getting confidence level of the classification the program uses 5 classifiers.Confidence level is based on the voting method.
 
