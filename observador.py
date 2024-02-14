class Sujeto:
    observadores = []
    def agregar(self, *args):
        self.observadores.append(*args)
    def quitar(self, obj):
        pass
    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)
class SujetoConcreto(Sujeto):
    def __init__(self): pass 
class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverA(Observador):
    def __init__(self):
        pass
        #self.observador_a = obj
        #self.observador_a.agregar(self, *args)
    def update(self,mensaje,*args):
        print("Actualización dentro de ObservadorConcretoA")
        
        print("Estos son los parametros: ", mensaje )

