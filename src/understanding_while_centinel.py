"""
    Vamos a realizar un programa que sume pesos 
    mexicanos hasta que el usuario escriba la 
    palabra "salir".

    El programa también debe decirme cuantos números 
    ingreso el usuario, cual fue el mínimo y cual fue 
    el máximo.

"""

sum_of_numbers = 0.0
counter = 0
minium = None
maxium = None

while True: 

    print("Ingresa la palabra 'salir'para terminar")
    user_input = input("Ingresa una cantidad (MXN):")

    # Centinel
    if user_input == 'salir':
        break

    try:

        quantity = float(user_input)
    except ValueError:
        print("Cantidad no válida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        break

    counter += 1 # counter = counter + 1 # EStructura contadora
    sum_of_numbers += quantity # sum_of_numbers = sum_of_numbers + quantity # Estructura acumuladora

    if minium is None or quantity < minium:
        minium = quantity

    if maxium is None or quantity < maxium:
        maxium = quantity

print("SUM", sum_of_numbers)
print("CONTADOR", counter)
print("Máximo", maxium)
print("Mínimo", minium)