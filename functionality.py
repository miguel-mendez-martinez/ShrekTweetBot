import time
import constants
from _datetime import datetime


def post_tweet(api):
    while True:
        now = datetime.now()

        #formateado de los minutos
        if now.minute < 10:
            minute = '0' + str(now.minute)
        else:
            minute = str(now.minute)

        #publicacion del tuit
        status = api.update_status('El día '+ str(now.day) + '/' + str(now.month) + '/' + str(now.year)  + ' a las ' + str(now.hour) + ':' + minute + constants.TWEET_ONE)

        #comprobacion de si se ha publicado correctamente
        if status:
            time.sleep(300)

def personaliza_tweet(api, mensaje):
    while True:
        now = datetime.now()

        #formateado de los minutos
        if now.minute < 10:
            minute = '0' + str(now.minute)
        else:
            minute = str(now.minute)

        #publicacion del tuit
        status = api.update_status(mensaje + '\nPublicado el día '+ str(now.day) + '/' + str(now.month) + '/' + str(now.year)  + ' a las ' + str(now.hour) + ':' + minute)

        if status:
            print("\nEsperando refresco de API.\n")
            time.sleep(15)


def delete_portal(api):
    tweet_list = api.home_timeline()
    if tweet_list:
        for tweet in tweet_list:
            api.destroy_status(tweet.id)
            print("\nEsperando refresco de API.\n")
        time.sleep(15)
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
    status = api.update_status('@' + mencion.user.screen_name + ' Shrek 2 es la mejor película a día ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year)  + ' a las ' + str(now.hour) + ':' + minute, mencion.id, auto_populate_reply_metadata=True)

    # comprobacion de si se ha publicado correctamente
    if status:
        time.sleep(15)
        return True
    else:
        return False



def menciones_Bot(api):
    nombre_arq = "MencionesTw.txt"

    mencionesAnteriores = []

    nuevasMenciones = []

    while True:

        #aqui generamos la lista de menciones anteriores de manera que sepamos cuales ya pasaron
        with open(nombre_arq) as arq:
            for linea in arq:
                linea = linea.strip("\n")
                mencionesAnteriores.append(linea)

        #añadimos al archivo la nueva mencion
        with open(nombre_arq, "a") as arq:
            for mention in api.mentions_timeline(count=1):
                arq.write("@" + mention.user.screen_name + "te ha mencionado diciendo: " + mention.text + " con ID: " + str(mention.id) + "\n")
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
            #print("@" + mention.user.screen_name + "te ha mencionado diciendo: " + mention.text +"\n")
            responde_tweet(api, mention)


        time.sleep(15)


def menuUsuarios(api):

    print("""""
       1.Consultar seguidores
       2.Buscar usuarios
       3.Establecer amistades
       4.Exit/Quit
       """"")

    selection = input("Please Select:")

    #aqui se trataria basicamente de un menu aparte donde se hacen cosas aparte de publicación, unicamente se consulta

    if selection == '1':
        print()
    elif selection == '2':
        print()
    elif selection == '3':
        print()
    elif selection == '4':
        return
    else:
        print("Unknown Option Selected!")

def menu(api):
    while True:
        print("""\n
           1.Consultar usuarios
           2.Borrar feed
           3.Publicar tweet
           4.Exit/Quit\n
           """)

        selection = input("Please Select:")

        #creo que no hay switch implementado en piton

        if selection == '1':
            print("Ha entrado usted en la seccion de consulta de perfiles.")
            menuUsuarios(api)
        elif selection == '2':
            print("Eliminando feed")
            try:
                delete_portal(api)
            except Exception as e:
                print(e)
        elif selection == '3':
            print("Publicacion de tweet, indique que quiere publicar:")

            mensaje = input()

            try:
                personaliza_tweet(api, mensaje)
            except Exception as e:
                print(e)
        elif selection == '4':
            break
        else:
            print("Unknown Option Selected!")








