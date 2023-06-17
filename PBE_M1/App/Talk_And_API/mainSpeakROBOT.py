from Talk_And_API.APIcall import *
#from APIcall import *
import datetime as dt
import sounddevice
import speech_recognition as sr
import subprocess
"""
import wikipediaapi
import requests
import json
"""


"""
......................................
......................................
......................................
......................................
......................................
......................................
"""

user_name="Personne"

list_news=None
apiNews=None
isNews=False
isStop=False

r = sr.Recognizer()
def get_input():
    with sr.Microphone(chunk_size=8912) as source:
        #r.adjust_for_ambient_noise(source) ----> choix qui laisse plus de temps d'attente
        r.energy_threshold=500

        r.adjust_for_ambient_noise(source,duration=0.8)
        #r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold=True
        r.pause_threshold=1.2

        ### vocal du robot
        respond("Je vous écoute!")
        ### vocal du robot

        print("Je vous écoute !")
        audio = r.listen(source,phrase_time_limit=5)
    try:
        input_text = r.recognize_google(audio,language="fr-FR")
        print(f"You said: {input_text}")
        return input_text
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, could not request results from Google Speech Recognition service: {e}")
        return ""

def initDump():
    say="espeak -vmb-fr1 -s 150 -a 80 {0} ".format("test")
    lst_say=say.split()
    subprocess.run(lst_say)

def respond(output_text):
    say="espeak-ng -vmb-fr1 -s 150 -a 80 -b 1"
    lst_say=say.split()
    lst_say.append('"{0}"'.format(output_text))
    subprocess.run(lst_say)


# mainloop
#while True:
def VoiceDialogue():
    input_text = get_input()
    print(f"voici ce qui a été dit ---> {input_text}")
    if input_text.lower() == "bonjour":
        respond("Bonjour {0}! Comment allez vous ?".format(user_name))
    elif input_text.lower() == "météo":
        #respond("Je suis désolé, je n'ai pas accès à internet pour vérifier la météo")
        respond(getTempAndHumToday())
    elif input_text.lower()=="quelle heure est-il":
        respond("il est "+str(dt.datetime.now().hour)+" heures "+str(dt.datetime.now().minute))
    elif "combien font " in input_text.lower():
        txt=input_text.lower().strip("combien font")
        val=0
        try:
            val=eval(txt.strip())
            respond("la réponse est "+ str(eval(txt.strip())) )
        except:
            respond("Répetez votre équation mathématique")

    elif input_text.lower()=="donne une nouvelle de la presse":
        #print(list_news)
        respond(apiNews.chooseRandomNews(list_news))

    elif input_text.lower() == "au revoir":
        respond("Au revoir ! Bonne journée à vous")
        ##### Variable
        return True
        isStop=True
    elif "qu'est-ce que" in input_text.lower():
        txt=input_text.lower().replace("Qu'est ce que","")
        txt=txt.strip()
        txt=txt.split()
        txt=str(txt[-1])
        print(txt)
        respond(WikiDefineThis(txt.strip()))
    elif input_text.lower()=="":
        pass
    else:
        respond("Je suis désolé, je n'ai pas compris ce que vous dites")


"""
while True:
    VoiceDialogue()
"""