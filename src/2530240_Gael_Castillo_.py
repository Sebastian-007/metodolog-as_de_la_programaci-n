# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

# Resumen Ejecutivo:
"""
En Python, una función es un bloque de código reutilizable que realiza una tarea específica. Las funciones se definen
utilizando la palabra clave "def", y permiten tener un código modular, legible y mantenible. Los parámetros son 
variables que se pasan a las funciones, mientras que los argumentos son los valores reales que se proporcionan a esos 
parámetros al llamar a la función. Separar la lógica en funciones reutilizables ayuda a mantener el código organizado 
y reduce la redundancia.Un valor de retorno es lo que una función devuelve al llamador, y es mejor devolver valores 
en lugar de solo imprimirlos, porque el resultado puede ser procesado o utilizado en otras partes del programa.

Este documento cubre el diseño de funciones para seis problemas, detallando las entradas, salidas, validaciones
 y casos de prueba para cada uno. También demostrará el uso de funciones en Python con el manejo adecuado de parámetros, 
 valores de retorno y comprobaciones básicas de errores.
"""

# Principios y buenas practicas
"""
- Preferir funciones pequeñas que hagan una sola cosa (single responsibility).
- Evitar repetir código: si copias/pegas lógica, considera extraerla en una función.
- Intentar que las funciones sean “puras” cuando sea posible (mismo input -> mismo output, sin efectos secundarios externos).
- Documentar con comentarios simples qué hace cada función y qué parámetros espera.
- Dar nombres claros a las funciones (calculate_bmi, not f1 o do_it).
"""

# Problem 1: Rectangle area and perimeter (basic functions)
"""
Description:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.

Inputs:
- width (float)
- height (float)

Salidas:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validations:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

Operaciones clave sugeridas:
- area = width * height
- perimeter = 2 * (width + height)


Test cases:
1) Normal: 
Ingresa el ancho del rectángulo: 2
Ingresa la altura del rectángulo: 3
Área: 6.0
Perímetro: 10.0

2) Border: 
Ingresa el ancho del rectángulo: 1
Ingresa la altura del rectángulo: 1
Área: 1.0
Perímetro: 4.0

3) Error: 
Ingresa el ancho del rectángulo: -2
Ingresa la altura del rectángulo: 5
Error: invalid input

"""
# Código
def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = float(input("Ingresa el ancho del rectángulo: "))
height = float(input("Ingresa la altura del rectángulo: "))

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    print(f"Área: {area}")
    print(f"Perímetro: {perimeter}")
else:
    print("Error: invalid input")



# Problem 2: Grade classifier (function with return string)
"""
Description:
Define una función classify_grade(score) que reciba una calificación numérica (0 a 100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Inputs:
- score (float o int)

Outputs:
- "Score:" <score>
- "Category:" <grade_letter>

Validations:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.

Operaciones clave sugeridas:
- if/elif para rangos.
- Función con un único return al final o varios returns (pero bien documentados).


Test cases:
1) Normal: 
Ingresa la calificación (0-100): 75
Score: 75.0
Category: C

2) Border: 
Ingresa la calificación (0-100): 1
Score: 1.0
Category: F

3) Error: 
Ingresa la calificación (0-100): -5
Error: invalid input

"""
# Código
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input("Ingresa la calificación (0-100): "))

if 0 <= score <= 100:
    grade = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {grade}")
else:
    print("Error: invalid input")



# Problem 3: List statistics function (min, max, average)
"""
Description:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), 
llamar la función y mostrar los valores.

Inputs:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Outputs:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validations:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- split() para construir la lista de strings.
- Conversión a float o int dentro de un ciclo.
- sum(), len(), min(), max() dentro de summarize_numbers().


Test cases:
1) Normal: 
Ingresa los números separados por coma: 10, 20, 30
Min: 10.0
Max: 30.0
Average: 20.0

2) Border: 
Ingresa los números separados por coma: 1, 2, 3
Min: 1.0
Max: 3.0
Average: 2.0

3) Error: 
Ingresa los números separados por coma: 
Error: invalid input

"""
# Código
def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
try:
    numbers_text = input("Ingresa los números separados por coma: ")
    numbers_list = [float(num) for num in numbers_text.split(",")]

    if numbers_list:
        stats = summarize_numbers(numbers_list)
        print(f"Min: {stats['min']}")
        print(f"Max: {stats['max']}")
        print(f"Average: {stats['average']}")
    else:
        print("Error: invalid input")
except: 
    print("Error: invalid input")



# Problem 4: Apply discount list (pure function)
"""
Description:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.

Inputs:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Outputs:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validations:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- Construir la lista de float desde texto.
- En la función, usar un ciclo para crear una nueva lista:
  - discounted_price = price * (1 - discount_rate)
- No modificar la lista de entrada (pure function).


Test cases:
1) Normal: 
Ingresa los precios separados por coma: 100, 200, 300
Ingresa la tasa de descuento (por ejemplo, 0.10 para 10%): 0.10
Original prices: [100.0, 200.0, 300.0]
Discounted prices: [90.0, 180.0, 270.0]

2) Border: 
Ingresa los precios separados por coma: 1, 1, 1
Ingresa la tasa de descuento (por ejemplo, 0.10 para 10%): 0.10
Original prices: [1.0, 1.0, 1.0]
Discounted prices: [0.9, 0.9, 0.9]

3) Error: 
Ingresa los precios separados por coma: 120, 150, 75
Ingresa la tasa de descuento (por ejemplo, 0.10 para 10%): 10
Error: invalid input

"""
# Código
def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

try:
    prices_text = input("Ingresa los precios separados por coma: ")
    prices_list = [float(price) for price in prices_text.split(",")]
    discount_rate = float(input("Ingresa la tasa de descuento (por ejemplo, 0.10 para 10%): "))

    if prices_list and 0 <= discount_rate <= 1:
        discounted_prices = apply_discount(prices_list, discount_rate)
        print(f"Original prices: {prices_list}")
        print(f"Discounted prices: {discounted_prices}")
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")



# Problem 5: Greeting function with default parameters
"""
Description:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos 
posicionales y nombrados.

Inputs:
- name (string)
- title (string opcional)

Outputs:
- "Greeting:" <greeting_message>

Validations:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().

Operaciones clave sugeridas:
- Uso de parámetros con valor por defecto: def greet(name, title=""):
- Uso de argumentos nombrados: greet(name="Alice", title="Dr.")


Test cases:
1) Normal: 
Ingresa tu nombre: gael sebastian castilo salazar
Ingresa tu título (opcional): soy ingeniero
Greeting: Hello, Soy Ingeniero Gael Sebastian Castilo Salazar!

2) Border: 
Ingresa tu nombre: gael sebastian castillo salazar
Ingresa tu título (opcional): 
Greeting: Hello, Gael Sebastian Castillo Salazar!

3) Error: 
Ingresa tu nombre: 
Ingresa tu título (opcional): gael
Error: invalid input

"""
# Código
def greet(name, title=""):
    return f"Hello, {title} {name}!" if title else f"Hello, {name}!"

name = input("Ingresa tu nombre: ")
title = input("Ingresa tu título (opcional): ")

if name.strip():
    greeting = greet(name, title)
    print(f"Greeting: {greeting.title()}")
else:
    print("Error: invalid input")


# Problem 6: Factorial function (iterative or recursive)
"""
Description:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, 
pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Inputs:
- n (int)

Outputs:
- "n:" <n>
- "Factorial:" <factorial_value>

Validations:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; si no se cumple, 
mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Versión iterativa:
  - result = 1
  - for i in range(1, n + 1): result *= i
- Versión recursiva (opcional):
  - factorial(0) = 1
  - factorial(n) = n * factorial(n - 1)


Test cases:
1) Normal: 
Ingresa un número entero (n) para calcular su factorial: 8
n: 8
Factorial: 40320

2) Border: 
Ingresa un número entero (n) para calcular su factorial: 2
n: 2
Factorial: 2

3) Error: 
Ingresa un número entero (n) para calcular su factorial: 
Error: invalid input

"""
# Código
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n = int(input("Ingresa un número entero (n) para calcular su factorial: "))

    if n >= 0:
        fact = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {fact}")
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")



# Conclusiones 
"""
Las funciones son una herramienta clave para organizar y reutilizar el código. Ayudan a dividir tareas complejas 
en bloques más simples y manejables, lo que mejora la legibilidad y el mantenimiento del código. Devolver valores 
con 'return' en lugar de solo imprimirlos proporciona mayor flexibilidad, ya que los resultados pueden ser utilizados 
o procesados por otras partes del programa en lugar de ser solo mostrados en la pantalla.El uso de parámetros y valores 
por defecto hace que las funciones sean más flexibles y reutilizables, ya que permite que se adapten a diferentes 
entradas sin necesidad de modificar el código cada vez. Encapsular la lógica en funciones fue útil especialmente en 
tareas repetitivas, como cálculos y validaciones. Esto redujo la redundancia y facilitó el manejo de casos especiales.
La diferencia entre la lógica principal y las funciones de apoyo quedó más clara al ver cómo las funciones 
ayudan a organizar tareas específicas dentro del programa, dejando la lógica principal para el flujo general del programa.
"""

# Referencias
"""
- https://realpython.com/defining-your-own-python-function/
- https://share.google/Vj2fxJD1ITfxkfS8k
- https://www.datacamp.com/es/tutorial/functions-python-tutorial
- https://youtu.be/hrv1ruHxiQY
- https://realpython.com/defining-your-own-python-function/
"""