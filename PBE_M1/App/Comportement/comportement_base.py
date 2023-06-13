class Sensor():
    def __init__(self,min_value,value_sensor,range_value):
        pass
    def LeverStatus(self):
        if(value_sensor>range_value):
            return True
        else:
            return False

class StatusNode():
    def __init__(self,triggerNode,nextNode,name):
        self.root=None
        self.triggerNode=triggerNode
        self.nextNode=nextNode
        self.name=name






"""
Les status présent sur le robot sont:
 ---> IDLE
    pas d'interaction que si qql intervient
 ---> SLEEPING
    permet d'être configuré uniquement sur l'adresse :
        172.30.40.62
 ---> ACTIVE
    Intervient de façon spontanné




"""