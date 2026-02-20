from matriz import Matriz
from utils import EscalarError, validar_escalar, validar_no_cero, EnteroError, validar_entero_positivo, DimensionError
############ TESTING #############

## FUNCIÓN PARA VALIDAR QUE LO INGRESADO SEA UN ENTERO

def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            validar_entero_positivo(valor)
            return valor
        
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
        
        except EnteroError as e:
            print(f"Error: {e}")

# MATRIZ 1
nombre1 = input("Ingrese nombre de la matriz: ")
filas1 = pedir_entero_positivo("Ingrese tamaño de filas: ")
columnas1 = pedir_entero_positivo("Ingrese tamaño de columnas: ")


m1 = Matriz(filas1, columnas1, nombre1)
m1.ingresar_datos()

print(m1)

# MATRIZ 2
nombre2 = input("Ingrese nombre de la matriz: ")
filas2 = pedir_entero_positivo("Ingrese tamaño de filas: ")
columnas2 = pedir_entero_positivo("Ingrese tamaño de columnas: ")

m2 = Matriz(filas2, columnas2, nombre2)
m2.ingresar_datos()

print(m2)

### OPERACIONES ENTRE MATRICES

print("\n OPERACIONES ENTRE MATRICES:")

try:
    print("Suma:")
    print(m1 + m2)
except DimensionError as e:
    print(f"Error en suma: {e}")

try:
    print("Resta:")
    print(m1 - m2)
except DimensionError as e:
    print(f"Error en resta: {e}")

try:
    print("Multiplicación:")
    print(m1 * m2)
except DimensionError as e:
    print(f"Error en multiplicación: {e}")

try:
    print("Hadamard:")
    print(m1.hadamard(m2))
except DimensionError as e:
    print(f"Error en Hadamard: {e}")

## PENDIENTE DE PRUEBA - SE PUSHEA SIN TESTEAR ##



## OPERACIONES DE MATRIZ POR ESCALAR


# MATRIZ 3 PARA PRUEBAS DE ESCALAR

nombre3 = input("Ingrese nombre de la matriz: ")
filas3 = pedir_entero_positivo("Ingrese tamaño de filas: ")
columnas3 = pedir_entero_positivo("Ingrese tamaño de columnas: ")


m3 = Matriz(filas3, columnas3, nombre3)
m3.ingresar_datos()

print(m3)

##PEDIR ESCALAR

while True:
    try:
        k = float(input("Ingresa la escalar: "))
        validar_escalar(k)
        validar_no_cero(k)
        break
    
    except ValueError:
        print("Debes ingresar un número.")
    
    except EscalarError as e:
        print(e)

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