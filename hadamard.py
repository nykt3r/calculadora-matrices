matrizA = []
matrizB = []

filasMatrizA = int(input('Ingrese el numero de filas de la matriz A: '))
columnasMatrizA = int(input('Ingrese el numero de columnas de la matriz A: '))

filasMatrizB = int(input('Ingrese el numero de filas de la matriz B: '))
columnasMatrizB = int(input('Ingrese el numero de columnas de la matriz B: '))

if columnasMatrizA == columnasMatrizB and filasMatrizA == filasMatrizB:

  for i in range(filasMatrizA):
    matrizA.append([])
    for j in range(columnasMatrizA):
      matrizA[i].append(
        int(input(f'MATRIZ A: Ingrese el elemento en la posición {i+1} , {j+1}: ')))


  print('\nEsta es tu matriz A\n')
  for fila in matrizA:
    print(fila)

  for i in range(filasMatrizB):
    matrizB.append([])
    for j in range(columnasMatrizB):
      matrizB[i].append(
        int(input(f'MATRIZ B: Ingrese el elemento en la posición {i+1} , {j+1}: ')))

  print('\nEsta es tu matriz B')
  for fila in matrizB:
    print(fila)

  def multiplicacion_hadamard(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] * B[i][j])
        result.append(row)
    return result

  resultado = multiplicacion_hadamard(matrizA, matrizB)

  print("\nResultado de la multiplicación Hadamard:")

  for fila in resultado:
    print(fila)
else:
  print('Las matrices no son compatibles para la multiplicación Hadamard.')
