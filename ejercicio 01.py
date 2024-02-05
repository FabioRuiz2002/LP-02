#gestion de inventario

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, cantidad)

    def quitar_producto(self, nombre, cantidad):
        if nombre in self.productos and self.productos[nombre].cantidad >= cantidad:
            self.productos[nombre].cantidad -= cantidad
            if self.productos[nombre].cantidad == 0:
                del self.productos[nombre]
        else:
            print("Producto no disponible en la cantidad solicitada.")

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(f"Producto: {producto.nombre}, Cantidad: {producto.cantidad}")