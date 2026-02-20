from utils import validar_misma_dimension, validar_producto, validar_escalar, validar_no_cero

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
                valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
                self.datos[i][j] = valor

    ## Operaciones entre matrices ##
    def __add__(self, matriz_b: Matriz): 
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] + matriz_b.datos[i][j]
        return resultado
    
    def __sub__(self, matriz_b: Matriz): 
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] - matriz_b.datos[i][j]
        return resultado
    
    def __mul__(self, matriz_b: Matriz):
        validar_producto(self, matriz_b)
        resultado = Matriz(self.filas, matriz_b.columnas)
        for i in range(self.filas):
            for j in range(matriz_b.columnas):
                for k in range(self.columnas):
                    resultado.datos[i][j] += self.datos[i][k] * matriz_b.datos[k][j]
        return resultado    
    
    def hadamard(self, matriz_b: Matriz):
        validar_misma_dimension(self, matriz_b)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] * matriz_b.datos[i][j]
        return resultado
    
    ## Operaciones por un escalar ##
    
    def suma_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] + k
        return resultado
    
    def resta_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] - k
        return resultado
    
    def multiplicacion_escalar(self, k):
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] * k
        return resultado
    
    def division_escalar(self, k):
        validar_no_cero(k)
        validar_escalar(k)
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.datos[i][j] = self.datos[i][j] / k
        return resultado