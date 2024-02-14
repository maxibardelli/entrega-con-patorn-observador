from dato import *
from pantalla import *
from observador import *
"""
def __main__():
    Pantalla(BaseDato("my_base.sqlite3").my_base)



if __name__=="__main__":
    __main__()
"""
"""este mundo me va a matar"""

class Controlador:
    def __init__(self,):
        self.app=Pantalla(BaseDato("my_base.sqlite3").my_base)
    def inicio_secion_observadorA(self,):
        self.observador=ConcreteObserverA(self.app.abmc)



if __name__ =="__main__":
    x=Controlador()
    x.incio_secion_observadorA()
    
