# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

#Resumen Ejecutivo:
"""
En Python, una **lista** es una colección ordenada y mutable de elementos, una **tupla** es similar 
pero inmutable, lo que significa que no se puede modificar después de su creación. Un **diccionario** 
es una colección de pares clave-valor, donde cada clave se asocia con un valor específico. 
La diferencia clave es que las listas y tuplas almacenan elementos en un orden, pero las listas pueden 
modificarse, mientras que las tuplas no. Los diccionarios, por su parte, usan claves únicas para 
acceder a sus valores.

Mi documento cubrirá la resolución de varios problemas prácticos usando **listas**, **tuplas** y **diccionarios**. 
Describiré cómo gestioné **entradas** y **salidas**, como la creación de listas de productos, el cálculo 
de distancias con tuplas y la administración de catálogos de productos y contactos con diccionarios. También 
incluiré las **validaciones** aplicadas, como verificar si los elementos están presentes en las colecciones y 
asegurar que los datos sean correctos antes de realizar cálculos. Utilizaré estos métodos en contextos prácticos 
como **registros de productos**, **estadísticas de estudiantes** y **frecuencia de palabras** en una oración.
"""

# Problem 1: Shopping list basics (list operations)
"""
Description:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).

Inputs:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

Operaciones clave sugeridas:
- split(), strip(), append(), len(), in.

Test cases:
1) Normal: 
Ingrese los productos iniciales separados por comas: tortillas, frijoles
Ingrese el producto a agregar: huevo
Ingrese el producto a buscar: tortillas
Items list: ['tortillas', 'frijoles', 'huevo']
Total items: 3
Found item: True

2) Border: 
Ingrese los productos iniciales separados por comas: manzana
Ingrese el producto a agregar: platano
Ingrese el producto a buscar: platano
Items list: ['manzana', 'platano']
Total items: 2
Found item: True

3) Error: 
Ingrese los productos iniciales separados por comas: apple, banana, orange
Ingrese el producto a agregar: pinapple
Ingrese el producto a buscar: cherry
Items list: ['apple', 'banana', 'orange', 'pinapple']
Total items: 4
Found item: False

"""
# Código
initial_items_text = input("Ingrese los productos iniciales separados por comas: ")
new_item = input("Ingrese el producto a agregar: ")
search_item = input("Ingrese el producto a buscar: ")

items_list = [item.strip() for item in initial_items_text.split(",")]
items_list.append(new_item.strip())
is_in_list = search_item.strip() in items_list

print(f"Items list: {items_list}")
print(f"Total items: {len(items_list)}")
print(f"Found item: {is_in_list}")


# Problem 2: Points and distances with tuples
"""
Description:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Inputs:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Outputs:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.

Operaciones clave sugeridas:
- Creación de tuplas: point_a = (x1, y1), point_b = (x2, y2)
- Cálculo de distancia: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
- Cálculo de punto medio: ((x1 + x2)/2, (y1 + y2)/2)


Test cases:
1) Normal: 
Ingrese las coordenadas del punto A (x1, y1): 3, 4
Ingrese las coordenadas del punto B (x2, y2): 4,4
Point A: (3.0, 4.0)
Point B: (4.0, 4.0)
Distance: 1.00
Midpoint: (3.5, 4.0)

2) Border: 
Ingrese las coordenadas del punto A (x1, y1): -3, 4
Ingrese las coordenadas del punto B (x2, y2): -3, 5
Point A: (-3.0, 4.0)
Point B: (-3.0, 5.0)
Distance: 1.00
Midpoint: (-3.0, 4.5)

3) Error: 
Ingrese las coordenadas del punto A (x1, y1): 
Error: invalid inputr: 

"""
# Código
x1, y1 = map(float, input("Ingrese las coordenadas del punto A (x1, y1): ").split(","))
x2, y2 = map(float, input("Ingrese las coordenadas del punto B (x2, y2): ").split(","))

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print(f"Distance: {distance:.2f}")
print(f"Midpoint: {midpoint}")


# Problem 3: Product catalog with dictionary
"""
Description:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.

Inputs:
- product_name (string).
- quantity (int; cantidad a comprar).

Outputs:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"

Validations:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).

Operaciones clave sugeridas:
- Definir dict literal: product_prices = {"apple": 10.0, ...}
- in para verificar existencia de clave.
- Acceso: unit_price = product_prices[product_name]

Test cases:
1) Normal: 
Ingrese el nombre del producto: banana
Ingrese la cantidad a comprar: 3
Unit price: 5.0
Quantity: 3
Total: 15.0

2) Border: 
Ingrese el nombre del producto: apple
Ingrese la cantidad a comprar: 1
Unit price: 10.0
Quantity: 1
Total: 10.0

3) Error: 
Ingrese el nombre del producto: 
Ingrese la cantidad a comprar: 3
Error: product not found

"""
# Código
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_name = input("Ingrese el nombre del producto: ").strip()
quantity = int(input("Ingrese la cantidad a comprar: "))

if product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price}")
else:
    print("Error: product not found")


# Problem 4: Student grades with dict and list
"""
Description:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Inputs:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Outputs:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Operaciones clave sugeridas:
- Diccionario de listas: grades = {"Alice": [90, 85], ...}
- sum(), len() para promedio.
- in para verificar clave.

Test cases:
1) Normal: 
Ingrese el nombre del estudiante: Bob
Grades: [78, 82, 84]
Average: 81.33
Passed: True

2) Border: 
Ingrese el nombre del estudiante: Alice
Grades: [90, 85, 88]
Average: 87.67
Passed: True

3) Error: 
Ingrese el nombre del estudiante: Charly
Error: student not found

"""
# Código
grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 82, 84],
    "Charlie": [92, 91, 94]
}

student_name = input("Ingrese el nombre del estudiante: ").strip()

if student_name in grades:
    student_grades = grades[student_name]
    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0
    print(f"Grades: {student_grades}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {is_passed}")
else:
    print("Error: student not found")


# Problem 5: Word frequency counter (list + dict)
"""
Description:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Inputs:
- sentence (string).

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validations:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Operaciones clave sugeridas:
- lower(), split()
- Recorrer la lista y actualizar el diccionario:
  - if word in freq_dict: freq_dict[word] += 1
  - else: freq_dict[word] = 1
- Uso de un ciclo para encontrar la palabra con mayor frecuencia.


Test cases:
1) Normal: 
Ingrese una oración: apple banana apple orange banana apple
Words list: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
Frequencies: {'apple': 3, 'banana': 2, 'orange': 1}
Most common word: apple

2) Border: 
Ingrese una oración: apple apple apple
Words list: ['apple', 'apple', 'apple']
Frequencies: {'apple': 3}
Most common word: apple

3) Error: 
Ingrese una oración: 
Error: invalid input

"""
# Código
sentence = input("Ingrese una oración: ").strip().lower()

words_list = sentence.split()

freq_dict = {}
for word in words_list:
    freq_dict[word] = freq_dict.get(word, 0) + 1

most_common_word = max(freq_dict, key=freq_dict.get)

print(f"Words list: {words_list}")
print(f"Frequencies: {freq_dict}")
print(f"Most common word: {most_common_word}")


# Problem 6: Simple contact book (dictionary CRUD)
"""
Description:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Inputs:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Outputs:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validations:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().

Operaciones clave sugeridas:
- Diccionario: contacts = {"Alice": "1234567890", ...}
- get(), in, pop()
- Estructura if/elif para manejar cada acción.


Test cases:
1) Normal: 
Enter action (ADD, SEARCH, DELETE): ADD
Enter contact name: David
Enter phone number: 82534
Contact saved: David, 82534

2) Border: 
Enter action (ADD, SEARCH, DELETE): SEARCH
Enter contact name: Alice
Phone: 1234567890

3) Error: 
Enter action (ADD, SEARCH, DELETE): DELETE
Enter contact name: Eve
Error: contact not found

"""
# Código
contacts = {"Alice": "1234567890", "Bob": "0987654321", "Charlie": "1122334455"}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: Invalid action")
else:
    name = input("Enter contact name: ").strip()

    if action_text == "ADD":
        if name and (phone := input("Enter phone number: ").strip()):
            contacts[name] = phone
            print(f"Contact saved: {name}, {phone}")
        else:
            print("Error: Name or phone cannot be empty")

    elif action_text == "SEARCH":
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            del contacts[name]
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")



# Principios y buenas practicas
"""
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
- Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
- Escribir código legible y mensajes claros para el usuario.
"""

# Conclusiones 
"""
Las listas, tuplas y diccionarios son como las herramientas básicas de Python. Las listas son perfectas 
cuando necesitas agregar o quitar cosas constantemente, como una lista de cosas por hacer. Las tuplas 
son para cuando no quieres que algo cambie, como las coordenadas de un punto. Los diccionarios son lo 
mejor cuando quieres buscar algo rápido usando claves, como si fueran etiquetas. Y cuando combinas estas 
estructuras, como diccionarios con listas, te ayudan a organizar datos más complejos de manera fácil, 
como un catálogo o las calificaciones de los estudiantes.
"""

# Referencias 
"""
- https://share.google/QHHEGucydIfuis11B
- https://share.google/Qwu3L4BKVVAtVq5yx
- https://share.google/uU9qfPeDYLDZJ4gM5
- https://share.google/A9wSlMRGUZ0lLt8yk
- https://share.google/4faaILEtydZtYEoZE
"""