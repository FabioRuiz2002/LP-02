#simulador de reservas de asientos de cine

class Cine:
    def __init__(self, filas, asientos_por_fila):
        self.sala = [['Libre' for _ in range(asientos_por_fila)] for _ in range(filas)]

    def reservar_asiento(self, fila, asiento):
        if self.sala[fila][asiento] == 'Libre':
            self.sala[fila][asiento] = 'Reservado'
            return True
        else:
            return False

    def mostrar_sala(self):
        for fila in self.sala:
            print(' '.join(fila))

def main():
    cine = Cine(5, 5)
    cine.mostrar_sala()
    print("Reservando asiento 3,3: ", cine.reservar_asiento(3, 3))
    print("Intentando reservar nuevamente el asiento 3,3: ", cine.reservar_asiento(3, 3))
    cine.mostrar_sala()

if __name__ == "__main__":
    main()