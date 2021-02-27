import json

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener


consumer_key = 'TIayHfHHr6XrWeCkNUGYieOJq'
consumer_secret = 'YdluvprHMCv66et1x0KgsxXjJGCsuc5bJKetdDkcOh68sOP6Ze'
access_token = '1321882927383367681-Q9oPCPU7YOHatYgz1Fnm8MVvKJNSQF'
access_token_secret = 'MCdil2C4DEzZ4F5QPydd1VVOo5GH26qnb4Oc6xZkp87E4'
# Create instance of our OAuthHandler, pass the consumer_key and the cosumer_secret, we 1st need to import it from tweepy
auth = OAuthHandler(consumer_key,
                    consumer_secret)

# Set access_token and access_token_secret to the handler, Use of set_access _token() function
auth.set_access_token(access_token, access_token_secret)

#Stream Handler - for this import StreamListener from tweepy.streaming module 
# Next we will subclass the StreamListener class in order to print the output directly to the console
class PrintListener(StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')
        # if not status.text[:3] == 'RT ':
        #     print(status.text)
        #     print(status.author.screen_name,
        #           status.created_at,
        #           status.source,
        #           '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # keep stream alive

#Access the twitter stream for this import Stream from tweepy
def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    #Tweets in English Language Only
    languages = ('en',)
    stream.sample(languages=languages)
    stream.sample()

# import module - API. Import module json 
def pull_down_tweets(screen_name):
    api = API(auth)
    # tweets = api.user_timeline(screen_name=screen_name, count=200)
    # To show only Taylor Swift's tweets select screen_name as her username
    tweets = api.user_timeline(screen_name='taylorswift13', count=50)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))

#Let's tell python that this code is meant to be run as a script, common way to do this is by using the following if condition

if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)