import time
import constants
import tweepy

def post_tweet(api):
    status = api.update_status(constants.TWEET_ONE)
    if(status):
        time.sleep(constants.HOUR)
        return True
    else:
        return False

def delete_portal(api):
    tweet_list = api.home_timeline()
    for tweet in tweet_list:
        api.destroy_status(tweet.id)

