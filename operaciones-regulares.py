from validadores import can_mult, can_sum_or_rest, input_positive_int

#Menú
def print_menu():
    print("\nOPERACIONES CON MATRICES")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")

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
def sum_matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

#Resta de matrices
def rest_matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

#Multiplicación de matrices
def mult_matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            row.append(suma)
        result.append(row)
    return result
    


#Inicio de ejecución
while True:
    print_menu()
    option = input("\nSelecciona una opción: ")

    if option == "4":
        print("¡Hasta luego!")
        break
    
    if option not in ("1", "2", "3"):
        print("\nOpción inválida")
        continue

    A = input_matrix("A")
    B = input_matrix("B")

    if option == "1":
        if can_sum_or_rest(A, B):
            result = sum_matrix(A, B)
        else:
            print("Error: Las matrices deben tener el mismo tamaño")
            continue
        
    elif option == "2":
        if can_sum_or_rest(A, B):
            result = rest_matrix(A, B)
        else:
            print("Error: Las matrices deben tener el mismo tamaño")
            continue
        
    elif option == "3":
        if can_mult(A, B):
            result = mult_matrix(A, B)
        else:
            print("Error: Columnas de A deben ser iguales a filas de B")
            continue

    print("\nResultado:")
    print_matrix(result)
