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
    return data["nom"],data["mail"],int(data["distance"]),data["mouvement"]




####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
####### CONSTANTE DE BASE POUR LE FICHIER CONFIG
name_user=""
mail_user=""
distance_choice_user=10
move_choice_user="Sinus"
name_user,mail_user,distance_choice_user,move_choice_user=ConfigData()

print(name_user,mail_user,distance_choice_user,move_choice_user)


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
list_news=apiNews.init_newsAPI()



## permet d'initialiser espeak-ng pour qu'il n'y a pas de soucis
#speakr.initDump()

#print(apiNews.chooseRandomNews(list_news))
#print(list_news)

"""
    LISTE DES PINS UTILISER:
        20 & 21 ---> servo moteur
        22 ---> photo-résistance
        2 & 3 ---> Capteur ultrason

        les 2 5Volts

        les GND UTILISEE ---> 39 & 6 & 9
"""



isNearRobot=False
isClicked=False
isAskedToStop=False

count_near=0

while(not isNearRobot):
    print(rcSensor.distance())
    #Verifie si quelqu'un s'approche du robot
    if(rcSensor.distance()<12):
        count_near=count_near+1
    if(count_near>3):
        isNearRobot=True

    time.sleep(0.2)
print("le robot est en écoute -- vous êtes proche du robot")

"""
Les dialogues possible :
    - Bonjour
    - Météo
    - Quelle heure est t-il
    - combien font <donner une équation mathématique simple>
    - qu'est ce que <donner un nom, un objet, un animal>


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
1) le robot attend que la personne soit prêt à l'aide du capteur ultrason
2) 3 interactions exisent
    a) avec la photo-résistance, il bouge le servo moteur
    b) avec le microphone, je peux faire plusieurs requêtes, telle que ---> horaire de train, météo et interaction basique
    c) comportement aléatoire , donne les news du journal

"""