cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)

# El condicional es el corazón de un if 
# Condicional
car = "bmw"
print(car == "bmw") # True

# Condicional False 
car = "Audi"
print(car == 'audi')

# Posible solucion a entrada del ususario
car = "Audi"
print(car.lower() == 'audi') # True

# Operador relacional != para determinar desigualdad 
requestred_topping = 'mushroom'
if requestred_topping != 'anchovies': # True
    print("Hold the anchovies!")

# Comparaciones númericas 
age = 18
print(age == 18) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta otra vez")

age = 17 
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Múltiples condiciones 
age_0 = 22
age_1 = 18
# Operación and
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 and age_1 >= 18) # True
# Operación or
print(age_0 >= 21 or age_1 >= 21) # True
print(age_0 >= 23 or age_1 >= 21) # False

"""
   Para preguntarnos si un valor especifico 
   esta en una lista podemos utilizar el 
   siguiente comparador:
   
   value in list
"""
motorcyycles = ["mortalica", "honda", "vento", "yamaha"]
moto_charly_wants = "italika"
print(moto_charly_wants in motorcyycles) # False
print("honda" in motorcyycles) # True   

"""
   Para preguntarnos si un valor especifico 
   NO esta en una lista podemos utilizar el 
   siguiente comparador:
   
   value not in list
"""
banned_students = ['jorge', 'carlos', 'moyra', 'luz', 'hots']
user = "mauro"
print(user not in banned_students) # True
print("jorge" not in banned_students) # False

## Variables del tipo booleano
game_active = True
can_edit = False

"""
   If statement

   sintax:

    if condition:
        do something

    if condition:
        do something
    else:
        do something 
"""

age = input("\n¿Dime cual es tu edad? ")
print(age)

if int(age) >= 18:
    print("Tu tienes la edad suficiente para votar")
else:
    print("Tu eres menor de edad, no puedes votar")
