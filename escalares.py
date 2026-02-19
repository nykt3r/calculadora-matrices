

#Menú
def print_menu():
    print("\nOPERACIONES CON ESCALAR")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. dividir")
    print("5. Salir")
    opcionMenu = input("\nSelecciona una opción: ")
    return opcionMenu

#Entrada de datos a matrices
def input_matrix(name):
    rows = input_positive_int(f"Ingresa el numero de filas de la matriz {name}: ")
    cols = input_positive_int(f"Ingresa el numero de columnas de la matriz {name}: ")
    matrix = []

    print(f"Ingrese los valores de la matriz {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"Elemento [{i}][{j}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("❌ Ingresa un número válido")
        matrix.append(row)

    return matrix

#Impresión de matrices
def print_matrix(matrix):
    for row in matrix:
        print(row)

#Suma de matrices
def suma_escalar(A, k):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + k)
        result.append(row)
    return result

#Resta de matrices
def resta_escalar(A, k):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - k)
        result.append(row)
    return result

#Multiplicación de matrices
def multiplicacion_escalar(A, k):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] * k)
        result.append(row)
    return result

def division_escalar(A, k):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] / k)
        result.append(row)
    return result
#Validaciones
def can_sum_or_rest(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])

def can_mult(A, B):
    return len(A[0]) == len(B)


def input_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("El número debe ser mayor que 0")
        except ValueError:
            print("Debes ingresar un número entero")

#Inicio de ejecución
while True:
    print_menu()
    option = input("\nSelecciona una opción: ")
    k = int(input('ingrese el numero de la escalar: '))


    if option == "5":
        print("¡Hasta luego!")
        break

    if option not in ("1", "2", "3","4"):
        print("\nOpción inválida")
        continue

    A = input_matrix("A")

    if option == "1":
        result = suma_escalar(A, k)

    elif option == "2":
      result = resta_escalar(A, k)

    elif option == "3":
      result = multiplicacion_escalar(A, k)

    elif option == "4":
      result = division_escalar(A, k)


    print("\nResultado:")
    print_matrix(result)