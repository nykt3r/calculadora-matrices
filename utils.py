class MatrizError(Exception):
    """Excepción base para errores de matrices"""
    pass


class DimensionError(MatrizError):
    pass


class NoCuadradaError(MatrizError):
    pass


class NoInvertibleError(MatrizError):
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
