class Sujeto:
    observadores = []
    def agregar(self, *args):
        self.observadores.append(*args)
    def quitar(self, obj):
        pass
    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)
class TemaConcreto(Sujeto):
    def __init__(self):
        self.estado = None
    def set_estado(self, value):
        self.estado = value
        self.notificar()
    def get_estado(self):
        return self.estado
class Observador(TemaConcreto):
    def update(self):
        raise NotImplementedError("Delegación de actualización")

class ConcreteObserverA(Observador):
    def __init__(self,obj,*args):
        self.observador_a = obj
        self.observador_a.agregar(self, *args)
    def update(self,*args):
        print("Actualización dentro de ObservadorConcretoA")
        
        print("Estos son los parametros: ", *args )
