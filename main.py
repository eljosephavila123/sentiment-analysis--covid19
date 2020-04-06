import sys
import tweepy

consumer_key='FZv7bY6C8ctED9YnX7vTIkhBZ'
consumer_secret='NdP7ZR3bcHUyAxbOkZhSpl5oHPMbqESbE52HlNhg1LdQIWSpGf'
access_key= '272478864-pNPAwmQiKcOGoAlcB2GoIK5FfgBc56ljiK5DmmEf'
access_secret='idsWxRpO05HclHbb9foOyrUQEjnZok1XlGQURYEvuczrV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'covid19' in status.text.lower():
            print (status.text)
            print('hello')

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-81.7506018328,-4.8869020311,-76.4140386761,1.4112460388])

