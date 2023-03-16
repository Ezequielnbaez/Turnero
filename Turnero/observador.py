class Tema:

    observadores = []

    def ingresar(self, obj):
        self.observadores.append(obj)

    def eliminar(self, obj):
        pass
    
    def notificar(self):
        for observador in self.observadores:
            observador.update()


class Observador:
    def update(self):
        raise NotImplementedError("Delegacion de actualizacion")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.ingresar(self)

    def update(self, *args):
        print("Actualizacion dentro de ObservadorConcretoA")
        self.estado = self.observador_a.get_estado()
        print("Notificación de estado = ", self.estado)




