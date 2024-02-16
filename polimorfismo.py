from abc import ABC, abstractmethod

#Creamos la clase

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡miau miau!"

#Creamos obejtos o instancias
perro = Perro()
gato = Gato()

#Método hacer_sonido en ambas clases
print(perro.hacer_sonido())
print(gato.hacer_sonido())