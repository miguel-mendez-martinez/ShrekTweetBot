import time
import constants
import tweepy


def post_tweet(api):
    now = datetime.now()

    #formateado de los minutos
    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)

    #publicacion del tuit
    status = api.update_status('El día '+ str(now.day) + '/' + str(now.month) + '/' + str(now.year)  + ' a las ' + str(now.hour) + ':' + minute + constants.TWEET_ONE)

    #comprobacion de si se ha publicado correctamente
    if(status):
        time.sleep(180)
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

