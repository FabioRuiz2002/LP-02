#Herencia multiple

class Forma:
    def dibujar(self):
        return "Dibujando forma"

class Color:
    def __init__ (self, color):
        self.color = color
    def pintar(self):
        return f"Pintando con {self.color}"

class CuadradoColorido(self, forma, color)
    def __init__ (self, color)
        super(). init()
        self.color
    def dibujar_y_pintar(slef):
        return f"{super().dibujar()}y{self.pintar()}"

#Creamos objetos o instancias
cuadrado = CuadradoColorido("rojo")

#Método dibujar_y_pintar
print(cuadrado.dibujar_y_pintar())