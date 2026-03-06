from matriz import Matriz
from utils import pedir_entero_positivo

# FUNCIONES AUXILIARES

def crear_matriz():
    print("\n=== CREAR MATRIZ ===")
    nombre = input("Nombre de la matriz: ")
    filas = pedir_entero_positivo("Número de filas: ")
    columnas = pedir_entero_positivo("Número de columnas: ")

    matriz = Matriz(filas, columnas, nombre)

    print("\n¿Cómo desea ingresar los datos?")
    print("1. Ingresar datos manualmente")
    print("2. Generar datos aleatorios")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        for i in range(filas):
            for j in range(columnas):
                while True:
                    try:
                        valor = float(input(f"Ingrese valor [{i}][{j}]: "))
                        matriz.datos[i][j] = valor
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido.")

    elif opcion == "2":
        matriz.ingresar_datos()

    else:
        print("Opción inválida. Se generarán datos aleatorios.")
        matriz.ingresar_datos()

    return matriz

def pedir_escalar():
    while True:
        try:
            k = float(input("Ingrese el valor del escalar: "))
            return k
        except ValueError:
            print("Error: Debes ingresar un número válido.")

