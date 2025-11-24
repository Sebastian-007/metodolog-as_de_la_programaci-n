"""
Hacer un programa que pregunte la edad de una persona
 y responda lo siguiente:
   - Si la edad es menor e igual a 4, entonces la entrada es gratuita.
   - Si la edad es menor e igual a 18, pero mayor que 4 entonces la entrada cuesta $200
   - Si la edad es mayor que 18, entonces la entrada cuesta $400.
"""
age = int(input("Por favor, ingresa tu edad: "))

if age <= 4:
    print("La entrada es gratuita.")
elif age <= 18 and age > 4:
    print("La entrada cuesta $200")
elif age > 18:
    print("la entrada cuesta $400")