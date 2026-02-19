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