from matriz import Matriz
############ TESTING #############

# MATRIZ 1
nombre1 = input("Ingrese nombre de la matriz: ")
filas1 = int(input("Ingrese tamaño de filas: "))
columnas1 = int(input("Ingrese tamaño de columnas: "))

m1 = Matriz(filas1, columnas1, nombre1)
m1.ingresar_datos()

print(m1)

# MATRIZ 2
nombre2 = input("Ingrese nombre de la matriz: ")
filas2 = int(input("Ingrese tamaño de filas: "))
columnas2 = int(input("Ingrese tamaño de columnas: "))

m2 = Matriz(filas2, columnas2, nombre2)
m2.ingresar_datos()

print(m2)

### OPERACIONES ENTRE MATRICES

print(m1+m2)
print(m1-m2)
print(m1*m2)
print(m1.hadamard(m2))

## PENDIENTE DE PRUEBA - SE PUSHEA SIN TESTEAR ##