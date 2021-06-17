
#simple consulta de los datos del usuario, conectando a la api y devolviendo un objeto user.
from credentials import CREDENTIALS
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CREDENTIALS['API_KEY'],
    CREDENTIALS['API_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'],
    CREDENTIALS['ACCESS_SECRET'])

api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    if user:
        print("The user is " + str(user.location) + ".")
        print("Authentication OK")
    else:
        print("Error during authentication")
except:
    print("Exception in autentification ocurred")
