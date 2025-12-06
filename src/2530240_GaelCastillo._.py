# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

#Resumen Ejecutivo:
"""
La serie de Fibonacci es una secuencia en la que cada término es la suma de los dos anteriores, comenzando con 
0 y 1. Calcular la serie hasta un número de términos n significa generar los primeros n elementos de la secuencia. 
El programa leerá el número n ingresado por el usuario, validará la entrada y generará la serie de Fibonacci 
utilizando un bucle (for o while). Luego, imprimirá la secuencia hasta el número de términos especificado.

"""

# Problem: Fibonacci series generator  
"""
Description:
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. 
La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.

Inputs:
- n (int; número de términos de la serie a generar).

Outputs:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validations:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.

Ejemplo de comportamiento esperado (no pegues el código completo, solo úsalo como referencia lógica):
- Entrada: n = 5
- Salida:
- Fibonacci series: 0 1 1 2 3

Test cases:  
1) Normal: 
Número de términos: 8
Serie de Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13]

2) Border: 
Número de términos: 1
Serie de Fibonacci: [0]

3) Error: 
Número de términos: 
Error: invalid input

"""

# Código
n = input("Número de términos: ")

try: 
    n = int(n)
except:
    print("Error: invalid input")
    exit()

if n < 1 or n > 50:
    print("Error: invalid input")
    exit()

fibonacci = []

if n >= 1:
    fibonacci.append(0)

if n >= 2:
    fibonacci.append(1)

for i in range(2, n):
    next_term = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_term)

print("Serie de Fibonacci:", fibonacci)



# Conclusiones 
"""
El uso de un bucle fue muy útil para generar la serie de Fibonacci, ya que nos permite calcular fácilmente 
el siguiente término sumando los dos términos anteriores de manera iterativa. Manejar los casos especiales 
para n = 1 y n = 2 es importante, ya que la salida para estos casos es única (la serie comienza de manera 
diferente que para valores mayores de n). Esta lógica se puede reutilizar en otros programas donde se 
requiera generar secuencias de números o procesos iterativos.
"""

# References:
"""
1) https://share.google/Jw3w1FywEvjT8KYEi
2) https://share.google/8meJRg5hjGlQkOFLT
3) https://share.google/KiHm5Lghw0Y0E7UC2
"""