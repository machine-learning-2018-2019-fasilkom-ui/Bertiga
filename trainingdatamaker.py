import tweepy
import csv 
import re

def clean_str(tweet):
    """
    Tokenization/tweet cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    tweet = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", tweet)
    return tweet.strip().lower()

consumer_key = 'ICxjRfEpvDm8XZWl2bBA6MbTj'
consumer_secret = 'qm5kdAjHLjSVNBoclAlzPVPAyJPTXmEhwCUdJixvdll5CmqRVz'
access_token = '1070195239707586560-wjbg5Rog9s8MX0ZuImdBXe0BUCLflQ'
access_token_secret = 'HVbRVALs3iwqSQKQ5k3QkLN4mms5GMd9AgVIa3H0kHxAg'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "Borderland 3",
                           count = 1000,
                           lang = "en").items():
									
    csvWriter.writerow([tweet.text.encode('utf-8')])
    print(tweet.text)
csvFile.close()