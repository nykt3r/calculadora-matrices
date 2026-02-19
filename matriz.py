class Matriz:

    def __init__(self, filas: int, columnas: int, nombre: str = ""):
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las dimensiones deben ser mayores a 0")

        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = [[0.0 for _ in range(columnas)] for _ in range(filas)]

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

############ Testeando creación de matriz e ingreso de datos: Exitoso

nombre = input("Ingrese nombre de la matriz: ")
filas = int(input("Ingrese tamaño de filas: "))
columnas = int(input("Ingrese tamaño de columnas: "))

m1 = Matriz(filas, columnas, nombre)
m1.ingresar_datos()

print(m1)