
# simple consulta de los datos del usuario, conectando a la api y devolviendo un objeto user.
import interface
from credentials import CREDENTIALS
import tweepy
import functionality
import threading
from interface import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CREDENTIALS['API_KEY'],
    CREDENTIALS['API_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'],
    CREDENTIALS['ACCESS_SECRET'])

api = tweepy.API(auth)

print("Hola soy " + api.me().name + " un bot de twitter, me actualizo cada hora publicando un tweet pero tengo mas funciones que desea hacer:")


# creamos los distintos hilos
hiloMenciones = threading.Thread(target=functionality.menciones_Bot, args=(api,))
hiloTweets = threading.Thread(target=functionality.post_tweet, args=(api,))

hiloMenu = threading.Thread(target=functionality.menu, args=(api,))

hiloInterfaz = threading.Thread(target=interface.inicial, args=(api,))

# hiloMenciones.start()
# hiloTweets.start()
# hiloMenu.start()
hiloInterfaz.start()

# hiloMenciones.join()
# hiloTweets.join()
# hiloMenu.join()
hiloInterfaz.join()

print("Todos los hilos han terminado con éxito")
