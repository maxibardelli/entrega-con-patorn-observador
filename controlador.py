from dato import *
from pantalla import *
from observador import ConcreteObserverA
from modelo import *
"""
def __main__():
    Pantalla(BaseDato("my_base.sqlite3").my_base)



if __name__=="__main__":
    __main__()
"""
"""este mundo me va a matar"""
"""
class Controlador:
    def __init__(self,):
        self.app=Pantalla(BaseDato("my_base.sqlite3").my_base)
        self.observador=ConcreteObserverA(Control())
        
x=Controlador()
x.observador
"""
def __main__():
    op1=ConcreteObserverA(Control())
    Pantalla(BaseDato("my_base.sqlite3").my_base)

if __name__=="__main__":
    __main__()
