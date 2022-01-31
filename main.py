import tweepy
import config


def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True


class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        if from_creator(status):
            print(status.text)
            print("https://twitter.com/twitter/status/" + str(status.id))


client = tweepy.Client(bearer_token=config.bearer_token)

api_key = config.api_key
api_secret_key = config.api_secret_key
access_token = config.access_token
secret_access_token = config.secret_access_token

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)

stream = IDPrinter(auth.consumer_key, auth.consumer_secret,
                   auth.access_token, auth.access_token_secret)

stream.filter(follow=[config.user_id])
