"""
   Vamos a realizar un programa que pregunte
   al usuario por su edad y muestre un mensaje
   diferente según el rango de edad en el que 
   se encuentre:
"""
try:
   age = int(input("Por favor, ingresa tu edad: "))
except:
   age = -1
   print("Tuviste un error, ingresaste un caracter no valido")

if age > 100:
   print ("Tienes mas de un siglo de vida")
elif age >= 18 and age <= 100:
   print ("Eres mayor de edad")
elif age < 18 and age >=0:
   print ("eres menor de edad")
else:

   print("Tuviste un error al ingresar la edad")

"""
Hacer un programa que pregunte la edad de una persona
 y responda lo siguiente:
   - Si la edad es menor e igual a 4, entonces la entrada es gratuita.
   - Si la edad es menor e igual a 18, pero mayor que 4 entonces la entrada cuesta $200
   - Si la edad es mayor que 18, entoncs la entrada cuesta $400.
"""

# Múltiple if

guisos = ["desebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
   print("Si hay asado")
else:
   print("No hay asado")
if "tamales" in guisos:
   print("Si hay tamales")
else:
   print("No hay tamales")
if "salsa verde" in guisos:
   print("Si hay salsa verde")
else:
   print("No hay salsa verde")