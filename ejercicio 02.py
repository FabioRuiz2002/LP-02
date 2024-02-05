#Registro de empleados y salarios

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

def registrar_empleado(lista_empleados):
    nombre = input("Introduce el nombre del empleado: ")
    salario = float(input("Introduce el salario del empleado: "))
    empleado = Empleado(nombre, salario)
    lista_empleados.append(empleado)

def mostrar_empleados(lista_empleados):
    for empleado in lista_empleados:
        print(f"Nombre: {empleado.nombre}, Salario: {empleado.salario}")

def main():
    lista_empleados = []
    while True:
        print("\n1. Registrar empleado")
        print("2. Mostrar empleados")
        print("3. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            registrar_empleado(lista_empleados)
        elif opcion == 2:
            mostrar_empleados(lista_empleados)
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()


        
    




        
