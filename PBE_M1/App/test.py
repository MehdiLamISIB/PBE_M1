import json

name=""

def ConfigData(name,mail,distace,movem):
    f=open('config.json',"r")

    data=json.loads(f.read())
    name=data["nom"]
    mail=data["mail"]
    distance=data["distance"]
    movem=data["mouvement"]
