from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob






# consumer key, consumer secret, access token, access secret.
ckey = "WIbLRlyDVrgDMkA5ocJ14y8m0" #Fake
csecret = "Z3VEPA8eqWHPoFdgsz0FjzgyLEbGcOVbP3qdDPegOby8ujEMyS" #fake
atoken = "83258656031903sfds40-0B6pZYqk7sKrjOlDKkWbWZe4yztnJiD"  #fake
asecret = "mOaa8Z8pHjyvGlHcdds5wxcsEfkPxjegFzwFAeCH0dkDrt4" #fake
 # create a dummy twitter app andget your own key,secret,token etc, all above are fake.


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = all_data["text"]
            blob=TextBlob(tweet)
            confidence=blob.polarity
            sentiment="positive"
            if(confidence<0):
                sentiment="negetive"
                confidence=abs(confidence)
            if(confidence*100>=30):
                output=open("twitter-out.txt","a")
                output.write(sentiment)
                output.write('\n')
                output.close()

            print(tweet,sentiment,confidence)
        except:
            pass

        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["news"])