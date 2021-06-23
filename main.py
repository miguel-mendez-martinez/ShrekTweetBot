
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

print("Hola soy " + api.me().name + " un bot de twitter, me actualizo cada hora publicando un tweet pero tengo mas funciones que desea hacer:")

while True:
    try:
        functionality.menciones_Bot(api)
    except Exception as e:
        print(e)




