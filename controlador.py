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
    def inicio_secion_observadorA(self,):
        self.observador=ConcreteObserverA(self.app.abmc)
        
    def __init__(self,):
        
        self.app=Pantalla(BaseDato("my_base.sqlite3").my_base)
        self.inicio_secion_observadorA(self.app)



if __name__ =="__main__":
    x=Controlador()
    #x.inicio_secion_observadorA()
      
