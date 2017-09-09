from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob






# consumer key, consumer secret, access token, access secret.
ckey = "WIbLRlyDVrgDMkA5o0J14x8m1"
csecret = "Z3VEPA8eqWHPoFUgsz0FjzgyLEbGcOVbP3qdDPegOby8ujEMyS"
atoken = "832586560319037440-0B6pZYqk7sKrjOlDKkWbWZe4yztnJiD"
asecret = "mOaa8Z8pHjyvGlHct5wxcsEfkPxjegFzwFAeCH0dkDrt4"


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