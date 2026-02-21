from matriz import Matriz
from utils import pedir_entero_positivo, NoCuadradaError

# print("=== CALCULO DE TRAZA ===")

# # Crear matriz
# nombre = input("Ingrese nombre de la matriz: ")
# filas = pedir_entero_positivo("Ingrese tamaño de filas: ")
# columnas = pedir_entero_positivo("Ingrese tamaño de columnas: ")

# m = Matriz(filas, columnas, nombre)

# # Ingresar datos
# m.ingresar_datos()

# print("\nMatriz ingresada:")
# print(m)

# # Calcular traza
# try:
#     traza = m.calcular_traza()
#     print("\nLa traza de la matriz es:", traza)
# except NoCuadradaError as e:
#     print("\nError:", e)

# print("\n=== CALCULO DE TRANSPUESTA ===")

# nombre = input("Ingrese nombre de la matriz: ")
# filas = pedir_entero_positivo("Ingrese tamaño de filas: ")
# columnas = pedir_entero_positivo("Ingrese tamaño de columnas: ")

# m = Matriz(filas, columnas, nombre)
# m.ingresar_datos()

# print("\nMatriz original:")
# print(m)

# transpuesta = m.calcular_transpuesta()

# print("\nMatriz transpuesta:")
# print(transpuesta)

print("\n=== CALCULO DE DETERMINANTE ===")

nombre = input("Ingrese nombre de la matriz: ")
filas = pedir_entero_positivo("Ingrese tamaño de filas: ")
columnas = pedir_entero_positivo("Ingrese tamaño de columnas: ")

m = Matriz(filas, columnas, nombre)
m.ingresar_datos()

print("\nMatriz ingresada:")
print(m)

try:
    det = m.calcular_determinante()
    print("\nEl determinante es:", det)

except NoCuadradaError as e:
    print("\nError:", e)