#import package
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tweepy
import re

# Store OAuth authentication credentials in relevant variables
access_token ='130747008-nlnIaUfCGw8aYajLFiKAxYMk1gyqemCrlEWHYDHh'
access_token_secret ='MuNC5IApriSimpYD4a0wcGVXh9TaB70BqCSXkjMuIKPct'
consumer_key = 'w3fRzD2YPNbyKepzTMpnNu5Hj'
consumer_secret = 'eeVtUHNGZY0g4IylbJbcnxs06FcOlaeXEcUBlO1NDotfBJ9yGB'

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#class listner
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

        # Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['arsenal','chelsea'])

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=(['text','lang']))

# Print head of DataFrame
print(df.head())

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Initialize list to store tweet counts
[arsenal, chelsea] = [0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    arsenal += word_in_text('arsenal', row['text'])
    chelsea += word_in_text('chelsea', row['text'])
  #  semarang += word_in_text('semarang', row['text'])
   # surabaya += word_in_text('surabaya', row['text'])

    # Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['arsenal', 'chelasea']

# Plot histogram
ax = sns.barplot(cd, [arsenal, chelsea])
ax.set(ylabel="count")
plt.show()

