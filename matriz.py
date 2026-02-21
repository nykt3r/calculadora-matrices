from utils import validar_misma_dimension, validar_producto, validar_division, validar_escalar, validar_cuadrada, validar_invertible

class Matriz:
    # Constructor: Valida tipo de datos y valores positivos para filas y columnas
    def __init__(self, filas: int, columnas: int, nombre: str = ""):
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las dimensiones deben ser mayores a 0")
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = [[0.0 for _ in range(columnas)] for _ in range(filas)]

    # Define la representacion en texto de un objeto
    def __str__(self):
        resultado = f"Matriz {self.nombre} ({self.filas}x{self.columnas}):\n"
        for fila in self.datos:
            resultado += "  ".join(map(str, fila)) + "\n"
        return resultado

    def ingresar_datos(self):
        print(f"Ingresando datos para la matriz {self.nombre}")
        for i in range(self.filas):
            for j in range(self.columnas):
                while True:
                    try:
                        valorStr = input(f"Elemento [{i+1}][{j+1}]: ")
                        valor = float(valorStr)
                        self.datos[i][j] = valor
                        break
                    except Exception as e:
                        print("Error:", e)
                        print("Intente nuevamente.\n")

## Operaciones entre matrices ##
    def __add__(self, matriz_b): 
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] + matriz_b.datos[i][j]
        return resultado
    
    def __sub__(self, matriz_b): 
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] - matriz_b.datos[i][j]
        return resultado
    
    def __mul__(self, matriz_b):
        validar_producto(self, matriz_b)
        resultado = Matriz(self.filas, matriz_b.columnas)
        for i in range(self.filas):
            for j in range(matriz_b.columnas):
                for k in range(self.columnas):
                    resultado.datos[i][j] += self.datos[i][k] * matriz_b.datos[k][j]
        return resultado    
    
    def hadamard(self, matriz_b):
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] * matriz_b.datos[i][j]
        return resultado
    
## Operaciones por un escalar ##
    def sumar_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] + k
        return resultado
    
    def restar_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] - k
        return resultado
    
    def multiplicar_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] * k
        return resultado
    
    def dividir_escalar(self, k):
        validar_escalar(k)
        validar_division(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] / k
        return resultado
    
## Operaciones elementales de matriz ##
    # Metodo auxiliar para calcular determinantes
    def obtener_menor(self, fila_excluir, columna_excluir):
        menor = Matriz(self.filas - 1, self.columnas - 1, self.nombre + "_menor")
        menor.datos = []
        for i in range(self.filas):
            if i == fila_excluir:
                continue
            nueva_fila = []
            for j in range(self.columnas):
                if j == columna_excluir:
                    continue
                nueva_fila.append(self.datos[i][j])
            menor.datos.append(nueva_fila)
        return menor
    
    def calcular_determinante(self):
        validar_cuadrada(self)
        # Caso matriz 1x1
        if self.filas == 1:
            return self.datos[0][0]
        # Caso matriz 2x2
        if self.filas == 2:
            return (
                self.datos[0][0] * self.datos[1][1]
                - self.datos[0][1] * self.datos[1][0]
            )
        # Caso general (recursivo)
        determinante = 0
        for j in range(self.columnas):
            elemento = self.datos[0][j]
            menor = self.obtener_menor(0, j)
            cofactor = ((-1) ** j) * elemento * menor.calcular_determinante()
            determinante += cofactor
        return determinante 
    
    def calcular_adjunta(self):
        validar_cuadrada(self)
        # Caso especial 1x1
        if self.filas == 1:
            adj = Matriz(1, 1, self.nombre + "_adj")
            adj.datos[0][0] = 1
            return adj
        # Paso 1: matriz de cofactores
        cofactores = Matriz(self.filas, self.columnas, self.nombre + "_cof")
        for i in range(self.filas):
            for j in range(self.columnas):
                menor = self.obtener_menor(i, j)
                signo = (-1) ** (i + j)
                cofactores.datos[i][j] = signo * menor.calcular_determinante()
        # Paso 2: transponer la matriz de cofactores
        adjunta = cofactores.calcular_transpuesta()
        adjunta.nombre = self.nombre + "_adj"
        return adjunta
    
    def calcular_inversa(self):
        validar_cuadrada(self)
        det = self.calcular_determinante()
        validar_invertible(det)
        adjunta = self.calcular_adjunta()
        inversa = Matriz(self.filas, self.columnas, self.nombre + "_inv")
        for i in range(self.filas):
            for j in range(self.columnas):
                inversa.datos[i][j] = adjunta.datos[i][j] / det
        return inversa
    
    def calcular_traza(self):
        validar_cuadrada(self)
        suma = 0
        for i in range(self.filas):
            suma += self.datos[i][i]
        return suma

    def calcular_transpuesta(self):
        resultado = Matriz(self.columnas, self.filas, self.nombre + "_T")
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[j][i] = self.datos[i][j]
        return resultado
