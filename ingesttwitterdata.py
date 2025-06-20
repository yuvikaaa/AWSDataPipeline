import tweepy
import boto3
import json
import time
import twittercred


topic = 'COVID'

if __name__ == '__main__':

    client = boto3.client('firehose')
    start_time = time.time()
    timeDiff = 0
    tweets = []
    while True:
        tweets = tweepy.Cursor(api.search, q=topic).items(1000)
        for tweet in tweets:
            response = client.put_record(
                DeliveryStreamName='kinesisyuvika',
                Record={
                    'Data': json.dumps(tweet._json) + '\n'
                }


            )
            print("Collecting Tweets....")
            print(response)
    