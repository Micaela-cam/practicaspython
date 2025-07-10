# calculadora con python cada opcion sera una funcion


def sumar(*numeros):
    return sum(numeros)

def restar(*numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return resultado

def multiplicar(*numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def dividir(*numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        resultado /= n
    return resultado

def potencia(base, exponente):
    return base ** exponente

def modulo(a, b):
    return a % b

# Historial de operaciones
historial = []

def mostrar_menu():
    print("\n CALCULADORA AVANZADA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Ver historial")
    print("0. Salir")

def pedir_numeros(cantidad=None):
    numeros = []
    while True:
        entrada = input("Introduce números separados por espacio: ")
        try:
            numeros = list(map(float, entrada.strip().split()))
            if cantidad and len(numeros) != cantidad:
                print(f" Debes introducir exactamente {cantidad} número(s).")
                continue
            return numeros
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                numeros = pedir_numeros()
                resultado = sumar(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"Sumar {numeros} = {resultado}")

            elif opcion == "2":
                numeros = pedir_numeros()
                resultado = restar(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"Restar {numeros} = {resultado}")

            elif opcion == "3":
                numeros = pedir_numeros()
                resultado = multiplicar(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"Multiplicar {numeros} = {resultado}")

            elif opcion == "4":
                numeros = pedir_numeros()
                resultado = dividir(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"Dividir {numeros} = {resultado}")

            elif opcion == "5":
                numeros = pedir_numeros(2)
                resultado = potencia(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"{numeros[0]} elevado a {numeros[1]} = {resultado}")

            elif opcion == "6":
                numeros = pedir_numeros(2)
                resultado = modulo(*numeros)
                print(f" Resultado: {resultado}")
                historial.append(f"{numeros[0]} módulo {numeros[1]} = {resultado}")

            elif opcion == "7":
                print("\n HISTORIAL:")
                if not historial:
                    print("No hay operaciones aún.")
                else:
                    for i, operacion in enumerate(historial, 1):
                        print(f"{i}. {operacion}")

            elif opcion == "0":
                print(" Saliendo de la calculadora. ¡Hasta luego!")
                break

            else:
                print(" Opción no válida. Elige un número del menú.")

        except ZeroDivisionError as e:
            print(f" Error: {e}")

        except Exception as e:
            print(f" Error inesperado: {e}")

if __name__ == "__main__":
    main()