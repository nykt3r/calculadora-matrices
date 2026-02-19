class Matriz:

    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos: list[list[float]] = []

    def __str__ (self):
        return f'La matriz "{self.nombre}" es de tamaño {self.filas}x{self.columnas}'

    def solicitar_valores(self):
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

m1 = Matriz(2,2,"A")

print(m1)