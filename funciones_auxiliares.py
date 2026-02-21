from matriz import Matriz
from utils import pedir_entero_positivo

# FUNCIONES AUXILIARES

def crear_matriz():
    print("\n=== CREAR MATRIZ ===")
    nombre = input("Nombre de la matriz: ")
    filas = pedir_entero_positivo("Número de filas: ")
    columnas = pedir_entero_positivo("Número de columnas: ")
    matriz = Matriz(filas, columnas, nombre)
    matriz.ingresar_datos()
    return matriz

def pedir_escalar():
    while True:
        try:
            k = float(input("Ingrese el valor del escalar: "))
            return k
        except ValueError:
            print("Error: Debes ingresar un número válido.")

