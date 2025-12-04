"""
    Vanos a realizar un programa que 
    defina un PIN como contraseña.

    Después vamos a darle 3 intentos 
    al ususario para escribir el pin.

    Si el usuario escribe correctamente 
    el pin , el programa debe mostrar 
    un mensaje de Acceso Permitido.

    Si el usuario se equivoca, el programa 
    debe decirle cuantos intentos le quedan
    y en caso de que no le queden intentos 
    el mensaje debe decir Acceso Denegado
    excediste tus intentos.
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3

intents = 0

while intents < MAX_ATTEMPTS:
    user_pin = input("Ingresa tu PIN: ")

    if user_pin == CORRECT_PIN:
        print("Acceso Permitido")
        break
    else:
        intents += 1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps > 0:
            print(f"PIN CORRECTO, te quedan {remaining_attemps} intentos")
        else:
            print("Acceso Permitido")