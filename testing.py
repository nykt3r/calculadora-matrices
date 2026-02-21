from matriz import Matriz
from utils import EscalarError, validar_entero_positivo, DimensionError, pedir_entero_positivo
############ TESTING #############

# # MATRIZ 1
# nombre1 = input("Ingrese nombre de la matriz: ")
# filas1 = pedir_entero_positivo("Ingrese tamaño de filas: ")
# columnas1 = pedir_entero_positivo("Ingrese tamaño de columnas: ")

# m1 = Matriz(filas1, columnas1, nombre1)
# m1.ingresar_datos()

# print(m1)

# # MATRIZ 2
# nombre2 = input("Ingrese nombre de la matriz: ")
# filas2 = pedir_entero_positivo("Ingrese tamaño de filas: ")
# columnas2 = pedir_entero_positivo("Ingrese tamaño de columnas: ")

# m2 = Matriz(filas2, columnas2, nombre2)
# m2.ingresar_datos()

# print(m2)

# ## OPERACIONES ENTRE MATRICES

# print("\n OPERACIONES ENTRE MATRICES:")

# try:
#     print("Suma:")
#     print(m1 + m2)
# except DimensionError as e:
#     print(f"Error en suma: {e}")

# try:
#     print("Resta:")
#     print(m1 - m2)
# except DimensionError as e:
#     print(f"Error en resta: {e}")

# try:
#     print("Multiplicación:")
#     print(m1 * m2)
# except DimensionError as e:
#     print(f"Error en multiplicación: {e}")

# try:
#     print("Hadamard:")
#     print(m1.hadamard(m2))
# except DimensionError as e:
#     print(f"Error en Hadamard: {e}")

## OPERACIONES DE MATRIZ POR ESCALAR

# MATRIZ 3 PARA PRUEBAS DE ESCALAR

nombre3 = input("Ingrese nombre de la matriz: ")
filas3 = pedir_entero_positivo("Ingrese tamaño de filas: ")
columnas3 = pedir_entero_positivo("Ingrese tamaño de columnas: ")


m3 = Matriz(filas3, columnas3, nombre3)
m3.ingresar_datos()

print(m3)

##PEDIR ESCALAR
## TRY-EXCEPT para dividir_escalar
while True:
    try:
        k = float(input("Ingresa la escalar: "))
        resultado_escalar = m3.dividir_escalar(k)
        print("Resultado de la división: ")
        print(resultado_escalar)
        break
    except ValueError:
        print("Debes ingresar un número.")
    except EscalarError as e:
        print("Error ESCALAR ", e)


##OPERACIONES

## SUMA

# resultado_escalar = m3.sumar_escalar(k)

# print("Resultado de la suma escalar:")
# print(resultado_escalar)

## RESTA

# resultado_escalar = m3.restar_escalar(k)

# print("Resultado de la resta escalar: ")
# print(resultado_escalar)

# ## MULTIPLICACIÓN:

# resultado_escalar = m3.multiplicar_escalar(k)
# print("Resultado de la multiplicación escalar: ")
# print(resultado_escalar)

