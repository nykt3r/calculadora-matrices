from historial import guardar_operacion
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
                print(A)
                B = crear_matriz()
                print(B)
                suma = A + B
                print("\nResultado: ", suma)
                guardar_operacion("Suma de matrices", suma)

            elif opcion == "2":
                A = crear_matriz()
                print(A)
                B = crear_matriz()
                print(B)
                resta = A - B
                print("\nResultado: ", resta)
                guardar_operacion("Resta de matrices", resta)

            elif opcion == "3":
                A = crear_matriz()
                print(A)
                B = crear_matriz()
                print(B)
                multiplicacion = A * B
                print("\nResultado: ", multiplicacion)
                guardar_operacion("Multiplicacion de matrices", multiplicacion)

            elif opcion == "4":
                A = crear_matriz()
                print(A)
                B = crear_matriz()
                print(B)
                hadamard = A.hadamard(B)
                print("\nResultado: ", hadamard)
                guardar_operacion("Producto Hadamard de matrices", hadamard)

            # Operaciones con escalar 
            elif opcion == "5":
                A = crear_matriz()
                print(A)
                k = pedir_escalar()
                suma_escalar = A.sumar_escalar(k)
                print("\nResultado: ", suma_escalar)
                guardar_operacion("Suma por un escalar", suma_escalar)

            elif opcion == "6":
                A = crear_matriz()
                print(A)
                k = pedir_escalar()
                resta_escalar = A.restar_escalar(k)
                print("\nResultado: ", resta_escalar)
                guardar_operacion("Resta por un escalar", resta_escalar)

            elif opcion == "7":
                A = crear_matriz()
                print(A)
                k = pedir_escalar()
                multiplicacion_escalar = A.multiplicar_escalar(k)
                print("\nResultado: ", multiplicacion_escalar)
                guardar_operacion("Multiplicacion por un escalar", multiplicacion_escalar)

            elif opcion == "8":
                A = crear_matriz()
                print(A)
                k = pedir_escalar()
                division_escalar = A.dividir_escalar(k)
                print("\nResultado: ", division_escalar)
                guardar_operacion("Division por un escalar", division_escalar)

            # Operaciones elementales
            elif opcion == "9":
                A = crear_matriz()
                print(A)
                determinante = A.calcular_determinante()
                print("\nDeterminante: ", determinante)
                guardar_operacion("Determinante", determinante)

            elif opcion == "10":
                A = crear_matriz()
                print(A)
                adjunta = A.calcular_adjunta()
                print("\nAdjunta: ", adjunta)
                guardar_operacion("Adjunta", adjunta)

            elif opcion == "11":
                A = crear_matriz()
                print(A)
                inversa = A.calcular_inversa()
                print("\nInversa: ", inversa)
                guardar_operacion("Inversa", inversa)

            elif opcion == "12":
                A = crear_matriz()
                print(A)
                traza = A.calcular_traza()
                print("\nTraza: ", traza)
                guardar_operacion("Traza", traza)

            elif opcion == "13":
                A = crear_matriz()
                print(A)
                transpuesta = A.calcular_transpuesta()
                print("\nTranspuesta: ", transpuesta)
                guardar_operacion("Transpuesta", transpuesta)

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