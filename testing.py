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



## OPERACIONES DE MATRIZ POR ESCALAR


# MATRIZ 3 PARA PRUEBAS DE ESCALAR

nombre3 = input("Ingrese nombre de la matriz: ")
filas3 = int(input("Ingrese tamaño de filas: "))
columnas3 = int(input("Ingrese tamaño de columnas: "))


m3 = Matriz(filas3, columnas3, nombre3)
m3.ingresar_datos()

print(m3)

##PEDIR ESCALAR

k = int(input("Ingresa la escalar para realizar operaciones: "))

##OPERACIONES

## SUMA

resultado_escalar = m3.suma_escalar(k)

print("Resultado de la suma escalar:")
print(resultado_escalar)

## RESTA

resultado_escalar = m3.resta_escalar(k)

print("Resultado de la resta escalar: ")
print(resultado_escalar)

## MULTIPLICACIÓN:

resultado_escalar = m3.multiplicacion_escalar(k)
print("Resultado de la multiplicación escalar: ")
print(resultado_escalar)

resultado_escalar = m3.division_escalar(k)
print("Resultado de la diviión: ")
print(resultado_escalar)