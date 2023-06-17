import requests
import os
import json
import random
#res=requests.get('https://newsapi.org/v2/top-headlines?country=be&apiKey=d2bf711bda434686a41f413c888ac175')




### Variable globals
alreadyGetNews=False
newsLIST=[]

def removeJson():
    if(os.path.isfile("news.json")):
        os.remove("news.json")



def init_newsAPI():
    json_data=getJSON_News()
    title_data=list_title(json_data)
    #print(title_data)
    return title_data



def chooseRandomNews(tab):
    item=random.choice(tab)
    title=item[0]+", source : "+item[1]
    return title


def getJSON_News():
    res=requests.get('https://newsapi.org/v2/top-headlines?country=be&apiKey=d2bf711bda434686a41f413c888ac175')
    if res.status_code==200:
        data=res.json()
        return data
    else:
        return "{}"
####DEBUG



def list_title(data):
    """
        La stucture consiste à avoir une liste ou chaque element sont
            [article du journal,presse]
    """
    list_news=list()
    for art in data['articles']:
        title=art['title'].split("-")
        #print(title)
        list_news.append(title)
    #print(list_news)
    return list_news


##### DEBUG FUCTION
##### DEBUG FUCTION
def show_json_new_data(data):
    for art in data['articles']:
        title=art['title']
        descr=art['description']
        source=art['source']['name']
        print("Titre",title)
        print("Description",descr)
        print("Source -->",source)
        print("---");
##### DEBUG FUCTION
##### DEBUG FUCTION




#init_newsAPI()



