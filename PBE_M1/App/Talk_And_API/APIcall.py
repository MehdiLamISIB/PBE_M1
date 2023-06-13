import requests
import json
import datetime as dt
import wikipediaapi


def WikiDefineThis(toDefine):
    try:
        WIKI_WIKI=wikipediaapi.Wikipedia('fr')
        page_wiki=WIKI_WIKI.page(toDefine)
        if(page_wiki.exists()):
            full_page = page_wiki.summary.split('.')
            if (len(full_page[0]) < 100):
                return "Selon Wikipédia, "+ '.'.join(full_page[0:2])
            else:
                return "Selon Wikipédia, "+full_page[0]
        else:
            return "Je n'ai pas de définition pour ce que vous demandez"
    except:
        return "Il y a un soucis avec Wikipédia"



def getTempAndHumToday():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=50.85&longitude=4.35&hourly=temperature_2m,relativehumidity_2m,apparent_temperature&forecast_days=1"
        headers = {'Accept': 'application/json'}
        response = requests.get(url,headers)
        meteo_Bruxelles=response.json()
        param_meteo=["time","temperature_2m","relativehumidity_2m","apparent_temperature"]
        meteoBxl=meteo_Bruxelles["hourly"]
        time_now = dt.datetime.now().hour
        response.close()
        return "la température à " + str(time_now) + "heures est de " + str(meteoBxl[param_meteo[1]][time_now]) + " degrès celsius et le ressentie est de " + str(meteoBxl[param_meteo[3]][time_now])+" degrès celsius."
    except:
        return "je n'ai pas pu obtenir les informations concernant la météo"

def getTrainToTime(ecart_temps):
    try:
        #gare centrale
        time=str(dt.datetime.now().hour)+str(dt.datetime.now().minute+ecart_temps)
        url = f"http://api.irail.be/liveboard/?station=Bruxelles-Central&lang=fr&format=json&time={time}"
        #print(url)
        # Tout les lignes ---> #"http://api.irail.be/liveboard/?id=BE.NMBS.008812005&lang=fr&format=json"
        headers = {'Accept': 'application/json'}
        response = requests.get(url,headers)
        train_data=response.json()
        train_listFrom_Central=train_data["departures"]["departure"]
        response.close()
        return train_listFrom_Central['0']["station"]+"a un delai de"+str(int(train["delay"]) / 60)
        """for train in train_listFrom_Central:
            print(train["station"],"a un delai de", str(int(train["delay"])/60) )
        """
    except:
        return "pas d'information à propos des trains"




#print( getTrainToTime(10) )

#print( getTempAndHumToday() )


##### DEBUG FUNCTION #####
##### DEBUG FUNCTION #####
def testgetTrainToTime(ecart_temps):
    #gare centrale
    time=str(dt.datetime.now().hour)+str(dt.datetime.now().minute+ecart_temps)
    url = f"http://api.irail.be/liveboard/?station=Bruxelles-Central&lang=fr&format=json&time={time}"
    #print(url)
    # Tout les lignes ---> #"http://api.irail.be/liveboard/?id=BE.NMBS.008812005&lang=fr&format=json"
    headers = {'Accept': 'application/json'}
    response = requests.get(url,headers)
    train_data=response.json()
    train_listFrom_Central=train_data["departures"]["departure"]

    for train in train_listFrom_Central:
        print(train["station"],"a un delai de", str(int(train["delay"])/60) )




def testgetTempAndHumToday():
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.85&longitude=4.35&hourly=temperature_2m,relativehumidity_2m,apparent_temperature&forecast_days=1"
    headers = {'Accept': 'application/json'}
    response = requests.get(url,headers)
    meteo_Bruxelles=response.json()
    param_meteo=["time","temperature_2m","relativehumidity_2m","apparent_temperature"]
    meteoBxl=meteo_Bruxelles["hourly"]
    time_now=dt.datetime.now().hour
    return "la température à"+str(time_now)+"heures est de ("+meteoBxl[param_meteo[1]][time_now]+" degrès celsius et ressentie est de "+meteoBxl[param_meteo[3]][time_now]
    """print("la température à",time_now,"heures est de (",meteoBxl[param_meteo[1]][time_now]," degrès celsius et ressentie est de ",meteoBxl[param_meteo[3]][time_now])
    print(dt.datetime.now().date())
    for i in range(len(meteoBxl["time"])):
        print("la température le ",meteoBxl[param_meteo[0]][i]," est de (",meteoBxl[param_meteo[1]][i],"°C et ressentie est de ",meteoBxl[param_meteo[3]][i],") , pour finir l'humidité apparente est de ",meteoBxl[param_meteo[2]][i],"%")
    """

##### DEBUG FUNCTION #####
##### DEBUG FUNCTION #####
##### DEBUG FUNCTION #####
##### DEBUG FUNCTION #####