class MatrizError(Exception):
    """Excepción base para errores de matrices"""
    pass


class DimensionError(MatrizError):
    pass


class NoCuadradaError(MatrizError):
    pass


class NoInvertibleError(MatrizError):
    pass

class EscalarError(MatrizError):
    pass

class EnteroError(MatrizError):
    pass


def validar_misma_dimension(A, B):
    if A.filas != B.filas or A.columnas != B.columnas:
        raise DimensionError("Las matrices deben tener las mismas dimensiones.")


def validar_producto(A, B):
    if A.columnas != B.filas:
        raise DimensionError("Columnas de A deben ser iguales a filas de B.")


def validar_cuadrada(A):
    if A.filas != A.columnas:
        raise NoCuadradaError("La matriz debe ser cuadrada.")


def validar_invertible(A):
    if A.determinante() == 0:
        raise NoInvertibleError("La matriz no es invertible (determinante = 0).")
    
def validar_no_cero(k):
    if k == 0:
        raise EscalarError("No se puede dividir por cero, ingresa otro número")

def validar_escalar(k):
    if not isinstance(k, (int, float)):
        raise EscalarError("El escalar debe ser un número.")

def validar_entero_positivo(valor):
    if not isinstance(valor, int):
        raise EnteroError("Debes ingresar un número entero.")
    
    if valor <= 0:
        raise EnteroError("El número debe ser mayor que 0.")