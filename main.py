
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

#while True:
#functionality.menciones_Bot(api)

while True:
    functionality.menciones_Bot(api)
    print("""""
       1.Consultar usuarios
       2.Borrar feed
       3.Publicar tweet
       4.Exit/Quit
       """"")
    print("Tiempo restante para siguiente tweet automatico--> ")

    selection = input("Please Select:")

    selection = 1

    if selection == '1':
        print()
    elif selection == '2':
        print("Eliminando feed")
        try:
            functionality.delete_portal(api)
        except Exception as e:
            print(e)
    elif selection == '3':
        print("Publicacion de tweet")
        try:
            while True:
                functionality.post_tweet(api)
        except Exception as e:
            print(e)
    elif selection == '4':
        break
    else:
        print("Unknown Option Selected!")


