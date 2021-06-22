import time
import constants
import tweepy


def post_tweet(api):
    status = api.update_status(constants.TWEET_ONE)
    if status:
        time.sleep(constants.HOUR)
        return True
    else:
        return False


def delete_portal(api):
    tweet_list = api.home_timeline()
    if tweet_list:
        for tweet in tweet_list:
            api.destroy_status(tweet.id)
        return True
    else:
        print("Tweet feed vacia no se podra borrar nada.")
        return False


def menciones_Bot(api):
    mentions_list = api.mentions_timeline(count=1)
    if mentions_list:
        for mention in mentions_list:
            print(mention.user.screen_name + "te ha mencionado, tal que: " + mention.text + "\n")
        return True
    else:
        return False

