from Talk_And_API import newsAPI as apiNews
#from Talk_And_API.APIcall import *
from Sensor import rc04_ultrason as rcSensor
from Sensor import photo_sensor as phSensor
from Sensor import two_servo_control as servoMovement
from Talk_And_API import mainSpeakROBOT as speakr
import time
import subprocess
import json
#### fonction pour lire fichier
def ConfigData():
    f=open('config.json',"r")
    data=json.loads(f.read())
    return data["nom"],data["mail"],int(data["distance"]),data["mouvement"],data["hibernate"],data["stop"]




####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
name_user=""
mail_user=""
distance_choice_user=10
move_choice_user="Sinus"
hibernate_robot="non"
stop_robot="non"
#name_user,mail_user,distance_choice_user,move_choice_user,hibernate_robot,stop_robot=ConfigData()

#print(name_user,mail_user,distance_choice_user,move_choice_user)



def GetSet_data_user():
    global name_user,mail_user,distance_choice_user,move_choice_user,hibernate_robot,stop_robot
    name_user,mail_user,distance_choice_user,move_choice_user,hibernate_robot,stop_robot=ConfigData()
    print("DATA "*10)
    print(name_user,mail_user,distance_choice_user,move_choice_user,hibernate_robot,stop_robot)
    print("DATA "*10)
#### Pour tester si changement marche et tt
"""while(True):
    name_user,mail_user,distance_choice_user,move_choice_user=ConfigData()
    print(name_user,mail_user,distance_choice_user,move_choice_user)
    time.sleep(5)
"""


####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG





##### Variable globals capteur

##### Variable globals API

""" A remttre après, je met en commentaires pour éviter d'utiliser de requetes API """
speakr.apiNews=apiNews
list_news=apiNews.init_newsAPI()
speakr.list_news=list_news


## permet d'initialiser espeak-ng pour qu'il n'y a pas de soucis
#speakr.initDump()

#print(apiNews.chooseRandomNews(list_news))
#print(list_news)

"""
    LISTE DES PINS UTILISER:
        20 & 21 ---> servo moteur
        22 ---> photo-résistance
        2 (trigger) & 3 (echo) ---> Capteur ultrason

        les 2 5Volts

        les GND UTILISEE ---> 39 & 6 & 9
"""



isNearRobot=False
isClicked=False
isAskedToStop=False

count_near=0




######## FIN INIT RASPI
######## FIN INIT RASPI
######## FIN INIT RASPI


def MainBehavior():
    global name_user,speakr
    """
    Cette fonction permet d'économiser des ressources en évitant de faire tourner du programme dans le vide
    """
    while(hibernate_robot=="oui"):
        GetSet_data_user()
        print("le robot est en hibernation, vous devez l'activer dans le formulaire")
        time.sleep(2)

    #### prend 2 param , count_near qui permet d'échantionner pour que le calcul distance soit bon
    ####               , retrieve_data_delay qui permet de rajouter du delai pour recup les données --> 5 pour 1 sec
    return ActivationBehavior(3,10)


def ActivationBehavior(count_near,retrieve_data_delay):
    global isNearRobot,rcSensor,distance_choice_user,stop_robot,hibernate_robot
    """
    Cette fonction attend que l'utilisateur vient pour activer le prochain niveau d'interaction
    """
    rdelay=0
    isNearRobot=False
    while(not isNearRobot):
        print(rcSensor.distance())
        #Verifie si quelqu'un s'approche du robot à la distance désiré par l'user
        if(rcSensor.distance()<distance_choice_user):
            count_near=count_near+1
        if(count_near>3):
            isNearRobot=True

        if(stop_robot=="oui"):
            # on arrete completement le robot
            os.exit();

        if(hibernate_robot=="oui"):
            ## on retourne dans le comportement d'économie
            return MainBehavior()

        ## permet de recup les données mais pas toute les 0.2 secondes
        if(rdelay > retrieve_data_delay):
           GetSet_data_user()
           rdelay=0
        rdelay=rdelay+1
        time.sleep(0.2)
    return TalkAndInteractBehavior()

def TalkAndInteractBehavior():
    global speakr,servoMovement,servo,stop_robot,hibernate_robot,isAskedToStop,list_news
    print("le robot est en écoute -- vous êtes proche du robot")
    while True:
        if(name_user!=""):
            speakr.user_name=name_user
        GetSet_data_user()
        #speakr.respond(apiNews.chooseRandomNews(list_news))

        ### Dialogue principale qui permet l'interaction
        isAskedToStop=speakr.VoiceDialogue()
        #speakr.VoiceDialogue()
        print("Loop talk")
        if(isAskedToStop):
            print("fin du process")
            speakr.respond("Je me met en mode hibernation")
            return MainBehavior()
        if(hibernate_robot=="oui"):
            speakr.respond("Je me met en mode Inactif, approchez vous pour interagir")
            return ActivationBehavior(3,10)
        if(stop_robot=="oui"):
            os.exit();
        time.sleep(0.2)


MainBehavior()

#### TOUT CE QUI EST EN DESSOUS EST EN TEMP
#### NORMALEMENT NE DEMMARE PAS


"""

while(not isNearRobot):
    print(rcSensor.distance())
    #Verifie si quelqu'un s'approche du robot à la distance désiré par l'user
    if(rcSensor.distance()<distance_choice_user):
        count_near=count_near+1
    if(count_near>3):
        isNearRobot=True

    time.sleep(0.2)
print("le robot est en écoute -- vous êtes proche du robot")


"""

"""
Les dialogues possible :
    - Bonjour
    - Météo
    - Quelle heure est t-il
    - combien font <donner une équation mathématique simple>
    - qu'est ce que <donner un nom, un objet, un animal>


"""



"""

while True:
    print("check")
    #speakr.respond(apiNews.chooseRandomNews(list_news))
    isAskedToStop=speakr.VoiceDialogue()
    print("check")
    if(phSensor.getPhotoResistorSignal()):
        print("hello world")
        ### le robot dit bonjour en bougant les servo moteurs
        servoMovement.HelloMove()
    if(isAskedToStop):
        print("fin du process")
        break



    time.sleep(0.5)

print("Le robot s'arrete --- ")
"""

"""
1) le robot attend que la personne soit prêt à l'aide du capteur ultrason
2) 3 interactions exisent
    a) avec la photo-résistance, il bouge le servo moteur
    b) avec le microphone, je peux faire plusieurs requêtes, telle que ---> horaire de train, météo et interaction basique
    c) comportement aléatoire , donne les news du journal

"""