import time
import constants
import datetime
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

def responde_tweet(api, mencion):
    now = datetime.now()

    # formateado de los minutos
    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)

    # publicacion del tuit
    status = api.update_status('@' + mencion.user.screen_name + 'yo tambien te quiero a dia' + str(now.day) + '/' + str(now.month) + '/' + str(now.year)  + ' a las ' + str(now.hour) + ':' + minute)

    # comprobacion de si se ha publicado correctamente
    if status:
        time.sleep(15)
        return True



def menciones_Bot(api):
    nombre_arq = "MencionesTw.txt"

    mencionesAnteriores = []

    nuevasMenciones = []

    #aqui generamos la lista de menciones anteriores de manera que sepamos cuales ya pasaron
    with open(nombre_arq) as arq:
        for linea in arq:
            linea = linea.strip("\n")
            mencionesAnteriores.append(linea)

    #añadimos al archivo la nueva mencion
    with open(nombre_arq, "a") as arq:
        for mention in api.mentions_timeline(count=1):
            arq.write("@" + mention.user.screen_name + "te ha mencionado diciendo: " + mention.text +"\n")

            #print(mention.user.screen_name + "te ha mencionado, tal que: " + mention.text + "\n")

    #creamos la lista de nuevas menciones, que serán recorrer el archivo acutalizado
    with open(nombre_arq) as arq:
        for linea in arq:
            linea = linea.strip("\n")
            nuevasMenciones.append(linea)

    #ahora comparamos ambas listas pasandolas a tipo set
    setMencionesAnt = set(mencionesAnteriores)
    setMencionesNuevas = set(nuevasMenciones)
    diferencia = setMencionesNuevas.difference(setMencionesAnt)

    #recorremos el nuevo set e imprimimos la nueva
    for mencion in diferencia:
        print(mention.text)
        responde_tweet(api, mention)

    time.sleep(15)





