#Menú
def print_menu():
    print("\nOPERACIONES MATRIZ")
    print("1. Transpuesta")
    print("2. Traza")
    print("3. Inversa")
    print("4. Determinante")
    print("5. Adjunta")
    print("6. Salir")
    opcionMenu = input("\nSelecciona una opción: ")
    return opcionMenu

#Validacion positivos
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


def validacion_traza(rows, cols):
  if rows != cols:
    print("La matriz no es cuadrada, no se puede calcular la traza.")

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
                    print("Ingresa un número válido")
        matrix.append(row)

    return matrix

#Impresión de matrices
def print_matrix(matrix):
    for row in matrix:
        print(row)

#Transponer matriz
def transpuesta_matriz(A):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[j][i])
        result.append(row)
    return result


def traza_matriz(A):
    validacion_traza(len(A), len(A[0]))
    result = 0
    for i in range(len(A)):
        result += A[i][i]
    return result
#Inicio de ejecución
while True:
    option = print_menu()

    if option == "6":
        print("¡Hasta luego!")
        break

    if option not in ("1", "2", "3", "4", "5"):
        print("\nOpción inválida")
        continue

    A = input_matrix("A")

    if option == "1":
        result = transpuesta_matriz(A)
    elif option == "2":
      result = traza_matriz(A)

    print("\nResultado:")
    print(result)
