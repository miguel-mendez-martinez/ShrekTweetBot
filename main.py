
#simple consulta de los datos del usuario, conectando a la api y devolviendo un objeto user.
from credentials import CREDENTIALS
import tweepy
import functionality
import threading
import constants

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CREDENTIALS['API_KEY'],
    CREDENTIALS['API_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'],
    CREDENTIALS['ACCESS_SECRET'])

api = tweepy.API(auth)

print("Hola soy " + api.me().name + " un bot de twitter, me actualizo cada hora publicando un tweet pero tengo mas funciones que desea hacer:")

#creamos los distintos hilos

hiloMenciones = threading.Thread(target=functionality.menciones_Bot, args=(api,))
hiloTweets = threading.Thread(target=functionality.post_tweet, args=(api,))

hiloMenu = threading.Thread(target=functionality.menu, args=(api,))

hiloMenciones.start()
hiloTweets.start()
hiloMenu.start()

hiloMenciones.join()
hiloTweets.join()
hiloMenu.join()

print("Todos los hilos han terminado con éxito")





