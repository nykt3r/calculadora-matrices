from matriz import Matriz
from utils import (
    pedir_entero_positivo,
    DimensionError,
    NoCuadradaError,
    NoInvertibleError,
    EscalarError
)

# FUNCIONES AUXILIARES

def crear_matriz():
    print("\n=== CREAR MATRIZ ===")
    nombre = input("Nombre de la matriz: ")
    filas = pedir_entero_positivo("Número de filas: ")
    columnas = pedir_entero_positivo("Número de columnas: ")
    matriz = Matriz(filas, columnas, nombre)
    matriz.ingresar_datos()
    return matriz

def pedir_escalar():
    while True:
        try:
            k = float(input("Ingrese el valor del escalar: "))
            return k
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def menu():
    print("\n" + "="*50)
    print("           CALCULADORA DE MATRICES")
    print("="*50)
    print("1. Sumar matrices")
    print("2. Restar matrices")
    print("3. Multiplicar matrices")
    print("4. Producto Hadamard")
    print("5. Sumar escalar")
    print("6. Restar escalar")
    print("7. Multiplicar por escalar")
    print("8. Dividir por escalar")
    print("9. Determinante")
    print("10. Adjunta")
    print("11. Inversa")
    print("12. Traza")
    print("13. Transpuesta")
    print("14. Salir")
    print("="*50)

# PROGRAMA PRINCIPAL

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        try:
            # Operaciones entre matrices 
            if opcion == "1":
                A = crear_matriz()
                B = crear_matriz()
                print("\nResultado:")
                print(A + B)

            elif opcion == "2":
                A = crear_matriz()
                B = crear_matriz()
                print("\nResultado:")
                print(A - B)

            elif opcion == "3":
                A = crear_matriz()
                B = crear_matriz()
                print("\nResultado:")
                print(A * B)

            elif opcion == "4":
                A = crear_matriz()
                B = crear_matriz()
                print("\nResultado:")
                print(A.hadamard(B))

            # Operaciones con escalar 
            elif opcion == "5":
                A = crear_matriz()
                k = pedir_escalar()
                print("\nResultado:")
                print(A.sumar_escalar(k))

            elif opcion == "6":
                A = crear_matriz()
                k = pedir_escalar()
                print("\nResultado:")
                print(A.restar_escalar(k))

            elif opcion == "7":
                A = crear_matriz()
                k = pedir_escalar()
                print("\nResultado:")
                print(A.multiplicar_escalar(k))

            elif opcion == "8":
                A = crear_matriz()
                k = pedir_escalar()
                print("\nResultado:")
                print(A.dividir_escalar(k))

            # Operaciones elementales
            elif opcion == "9":
                A = crear_matriz()
                print("\nDeterminante:")
                print(A.calcular_determinante())

            elif opcion == "10":
                A = crear_matriz()
                print("\nAdjunta:")
                print(A.calcular_adjunta())

            elif opcion == "11":
                A = crear_matriz()
                print("\nInversa:")
                print(A.calcular_inversa())

            elif opcion == "12":
                A = crear_matriz()
                print("\nTraza:")
                print(A.calcular_traza())

            elif opcion == "13":
                A = crear_matriz()
                print("\nTranspuesta:")
                print(A.calcular_transpuesta())

            elif opcion == "14":
                print("\nGracias por usar el programa 👋")
                break

            else:
                print("\nOpción inválida.")

        # Manejo de errores
        except DimensionError as e:
            print("\nError de dimensión:", e)

        except NoCuadradaError as e:
            print("\nError:", e)

        except NoInvertibleError as e:
            print("\nError:", e)

        except EscalarError as e:
            print("\nError:", e)

        except Exception as e:
            print("\nError inesperado:", e)

        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()