from random import choice 
from experta import *

class Light(Fact):
    """Informacion acerca de la luza de semforo"""
    pass

class RobotCruzaCalle(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print ('Caminar')

    @Rule(Light(color='red'))
    def red_light(self):
        print ('No cruzar la pista')

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def precaucion(self,light):
        print ('Gurda... ten cuidado la luz es ta en ', light['color'])


engine = RobotCruzaCalle()

engine.reset()
engine.declare(Light(color=choice(['green','yellow','blinking-yellow','red'])))
engine.run()




