from indicoio import config, sentiment, batch_sentiment
import csv

config.api_key = "0285e71c8c80f055c102ad5f3a614fc2"

tweets=[]

with open('twitter_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        tweets.append(row[1]) 

del(tweets[0])

batch = batch_sentiment(tweets)

for element in batch:
	if(element>0.5):
		print "Postive",
		print ",",
	else:
		print "Negative",
		print ",",
	print element
