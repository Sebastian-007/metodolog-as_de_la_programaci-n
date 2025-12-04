"""
    Docstring for understanding_while

    Utilizamos el while loop para ejecutar un bloque
    de código mientras una condición sea verdadera.

    Estructura básica del while loop en Python:

        while condición: 
            #Bloque de código a ejecutar

"""

# Ejemplo básico de un while loop
# Verificar si un número esta en un
# rango especifico (10 y entre 20)

while True: # while loop infinito
    try:
        number = int(input("Ingresa el número entre el 10 y 20: "))

        if number < 20 and number > 10:
            print("Número dentro del rango, Felicitaciones!")
            break
        else:
            print("Entrada invalida, por favor ingrese un número entero. ")
    except ValueError:
        print("Entrada inválida, porfavor ingrse un número entero.")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break

print("Saliste del while")