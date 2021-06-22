
#simple consulta de los datos del usuario, conectando a la api y devolviendo un objeto user.
from credentials import CREDENTIALS
import tweepy
import functionality
import constants

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CREDENTIALS['API_KEY'],
    CREDENTIALS['API_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'],
    CREDENTIALS['ACCESS_SECRET'])

api = tweepy.API(auth)

#hola roque esto es para comprobar cosas

try:
    while True:
        functionality.post_tweet(api)
    #functionality.delete_portal(api)
    #functionality.post_tweet(api)
except Exception as e:
    print("EXCEPTION-> " + e)
