from matriz import Matriz
from menu import iniciar_menu
from funciones_auxiliares import crear_matriz, pedir_escalar
from utils import (
    DimensionError,
    NoCuadradaError,
    NoInvertibleError,
    EscalarError
)

# PROGRAMA PRINCIPAL
def main():
    while True:
        iniciar_menu()
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