import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("<API_Key>", "<API secret key>")
auth.set_access_token("<Access_Token>","<Access token secret>")
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
