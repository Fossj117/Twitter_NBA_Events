from slistener import SListener
import time, tweepy, sys

## authentication
# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret=''
access_token=''
access_token_secret=''

 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def main():
    track = ["#NBAFinals", "@MiamiHEAT", "@Spurs"] 
    prefix = 'NBAFinals'

    listen = SListener(api, prefix)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
