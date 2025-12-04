# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

# Resumen Ejecutivo:
"""
En Python, la mayoría de los tipos de datos integrados son inmutables, como int, float, bool, str, bytes y tuple, lo que significa que no 
pueden modificarse una vez creados. También existen tipos mutables, como listas y diccionarios, que sí permiten cambiar sus elementos.
Además, Python incluye varios tipos de operadores, como aritméticos, relacionales, lógicos, de asignación, bit a bit, de pertenencia 
y de identidad, que permiten realizar cálculos, comparaciones y verificaciones dentro del código.

Hablando desde mi punto de vista, es importante validar y normalizar texto de entrada ya que nos da una mejor presentacion, orden y demas, 
tambien ayuda a el programador tenga un mejor control y manejo de la informacion.

Mi documento cubre el manejo de strings, comparando, validanndo, etc. los metodos que se usaran son:len(), indexación (text[i]), slicing (text[a:b]), 
lower(), upper(), title(), strip(), replace(), split(), join(), startswith(), endswith(), find(), operadores: f"" (f-strings), + (concatenación), 
* (repetición), in / not in (búsqueda simple), == (comparación).
"""

# Problem 1: Full name formatter (name + initials)
"""
Description: Dado el nombre completo de una persona en una sola cadena (por ejemplo: "gael sebastian castillo"), el programa debe:
normalizar el texto (strip, espacios extra, mayúsculas/minúsculas) y mostrar el nombre formateado en Title Case y las iniciales 
(por ejemplo: G.S.C.).

Inputs:
    - full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).

Outputs:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"


Validations:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
    - No aceptar cadenas que sean solo espacios.

Operaciones clave sugeridas: strip(), split(), title(), concatenación, len().


Test cases:
1) Normal: 
Ingresa tu nombre completo: gael sebastian castillo salazar
Formatted name: Gael Sebastian Castillo Salazar
Initials: G.S.C.S.

2) Border:
Ingresa tu nombre completo: gael castillo
Formatted name: Gael Castillo
Initials: G.C.

3) Error:
Ingresa tu nombre completo: gael
Error: Must contain at least 2 words

"""
#Código:
full_name = input("Ingresa tu nombre completo: ")
if len(full_name) == 0:
    print("Error: El nombre no puede estar vacío.")
elif len(full_name.split()) < 2:
    print("Error: Must contain at least 2 words")
else: 
    full_name_2 = full_name.strip().title().split()
    full_name_3 = " ".join(full_name_2)
    print(f"Formatted name:", full_name_3 )
    initials = ".".join([initial [0]for initial in full_name_2]) + "."
    print("Initials:", initials )



# Problem 2: Simple email validator (structure + domain)
"""
Description: Valida si una dirección de correo tiene un formato básico correcto:
    - Contiene exactamente un '@'.
    - Después del '@' debe haber al menos un '.'.
    - No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').


Inputs:
    - email_text (string).

    
Outputs:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"

    
Validations:
    - email_text no vacío tras strip().
    - Contar cuántas veces aparece '@'.
    - Verificar que no haya espacios (no debe haber " " en email_text).

Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in.


Test cases:
1) Normal: 
Ingresa tu correo electrónico:gaelcastillo@gmail.com
Valid email: True
Domain: gmail.com

2) Border: 
Ingresa tu correo electrónico:g@.gmai.com
Valid email: True
Domain: .gmai.com

3) Error: 
Ingresa tu correo electrónico:gaelcastillo.gmail.com
Valid email: False

"""
# Código:
print("Formato: username@.gmail.com")
print("Después del '@' debe haber al menos un '.'")
email_text = input("Ingresa tu correo electrónico:")
email_text = email_text.strip()
at_sign = email_text.find("@")
domain_part = email_text[at_sign + 1:]
if not email_text or email_text.count("@") != 1 or " " in email_text or "."not in domain_part: 
    print("Valid email:", False)
else:
    print("Valid email:", True)
    print("Domain:", domain_part)


# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Description: Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda,
ignorando espacios y mayúsculas/minúsculas.

    Ejemplos:
        - "Anita lava la tina" -> palíndromo.
        - "Hola mundo" -> no palíndromo.


Inputs:
    - phrase (string).


Outputs:
    - "Is palindrome: true" o "Is palindrome: false"
    - (Opcional) Mostrar también la versión normalizada de la frase.

    
Validations:
    - phrase no vacía tras strip().
    - Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.


Test cases:
1) Normal: 
Ingresa una frase: anita lava la tina
Is palindrome: True

2) Border: 
Ingresa una frase: anITa lAva lA tINa
Is palindrome: True

3) Error: 
Ingresa una frase:    
Is palindrome: False


"""
#Código
phrase = input("Ingresa una frase: ")
phrase = phrase.strip().lower().replace(" ", "")
reversed_phrase = phrase[::-1]

if not phrase:
    print("Is palindrome:", False)
    phrase 
elif phrase != reversed_phrase:
    print("Is palindrome:", False)
else:
    print("Is palindrome:", True)

# Problem 4: Sentence word stats (lengths and first/last word)
"""
Description: Dada una oración, el programa debe:
    1) Normalizar espacios (quitar espacios al principio y al final).
    2) Separar las palabras por espacios.
    3) Mostrar:
       - Número total de palabras.
       - Primera palabra.
       - Última palabra.
       - Palabra más corta y más larga (por longitud).

Inputs:
    - sentence (string).


Outputs:
    - "Word count: <n>"
    - "First word: <...>"
    - "Last word: <...>"
    - "Shortest word: <...>"
    - "Longest word: <...>"

Validations:
    - Oración no vacía tras strip().
    - Debe contener al menos una palabra válida después de split().

Operaciones clave sugeridas: strip(), split(), len(), recorrer la lista de palabras para encontrar mínima y máxima longitud.


Test cases:
1) Normal: gael
Ingresa una oración: Hola como estas
Word count: 3
First word: Hola
Last word: estas
Shortest word: Hola
Longest word: estas

2) Border: 
Ingresa una oración: gael
Word count: 1
First word: gael
Last word: gael
Shortest word: gael
Longest word: gael

3) Error: 
Ingresa una oración:    
Write a sentence

"""
#Código
sentence = input("Ingresa una oración: ")
sentence = sentence.strip().split()
if not sentence or len(sentence) < 1:
    print("Write a sentence")
else:
    words = len(sentence)
    first_word =sentence[0]
    last_word =sentence[-1]
    short_word = min(sentence, key = len)
    long_word = max(sentence, key = len)
    print("Word count:", words)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", short_word)
    print("Longest word:", long_word)

# Problem 5: Password strength classifier
"""
Description: Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, 
pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).


Inputs:
    - password_input (string).


Outputs:
    - "Password strength: weak"
    - "Password strength: medium"
    - "Password strength: strong"


Validations:
    - No aceptar contraseña vacía.
    - Verificar longitud con len().

Operaciones clave sugeridas:
- Recorrer carácter por carácter.
- Métodos: isupper(), islower(), isdigit(), isalnum().
- Uso de banderas booleanas (has_upper, has_lower, etc.).


est cases:
1) Normal: 
Ingresa una contraseña: gael123
Password strength: weak

2) Border: 
Ingresa una contraseña: Gaelsebcas#15
Password strength: strong

3) Error: 
Ingresa una contraseña:     
Error: ingresa una contraseña porfavor.

"""
# Código 
password_input = input("Ingresa una contraseña: ")
password_input = password_input.strip()


if len(password_input) == 0:
    print("Error: ingresa una contraseña porfavor.")
else: 
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    length = len(password_input)
    if length >= 8 and has_lower and has_upper and has_digit and has_symbol:
            print("Password strength: strong")
    elif length >= 8 and (has_lower or has_upper) and has_digit:
        print("Password strength: medium")
    else:
            print("Password strength: weak")

# Problem 6: Product label formatter (fixed-width text)
"""
Description: Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

    Product: <NAME> | Price: $<PRICE>

    La cadena completa debe tener exactamente 30 caracteres:
        - Si es más corta, rellena con espacios al final.
        - Si es más larga, recorta hasta 30 caracteres.


Inputs:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).
 
Outputs:
    - "Label: <exactly 30 characters>"
    (Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validations:
    - product_name no vacío tras strip().
    - price_value debe poder convertirse a un número positivo.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.


Test cases:
1) Normal: 
Ingresa el nombre del producto: pan
Ingresa el precio de tu producto: 8
Product: pan| Price: $8.0     

2) Border: 
Ingresa el nombre del producto: camioneta
Ingresa el precio de tu producto: 300000
Product: camioneta| Price: $30

3) Error: 
Ingresa el nombre del producto: 
Invalido: Por favor ingresa el nombre del producto: 

"""
#Código
product_name = input("Ingresa el nombre del producto: ")
product_name = product_name.strip()

if len(product_name) == 0:
    print("Invalido: Por favor ingresa el nombre del producto: ")
else: 
    try:
        price_value = float(input("Ingresa el precio de tu producto: "))

        if price_value < 0:
            print("Ingresa un precio valido, no puede ser negativo")
        else:
            product_name_and_price = f"Product: {product_name}| Price: ${price_value}"

        if len(product_name_and_price) < 30: 
            product_name_and_price = product_name_and_price + (" " * (30 - len(product_name_and_price)))
            print(product_name_and_price)
        else: 
            product_name_and_price = product_name_and_price[:30]
            print(product_name_and_price)
    except: 
        print("Error: invalid value")

"""
Principios y buenas prácticas:
    - Los strings son inmutables: cualquier cambio genera una nueva cadena.
    - Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
    - Evitar "números mágicos" en índices; documentar qué extrae cada slice.
    - Usar métodos de string en lugar de reescribir lógica básica.
    - Diseñar validaciones claras: primero que no esté vacío, luego el formato.
    - Escribir código legible: nombres de variables claros y mensajes de error entendibles.

"""

# Conclusiones 
"""
En mi documento se practico, se investigo y se llevo a cabo el manejo de strings, se aprendio 
a manejar los metodos de strings, concatenacion y el uso de bloques como: try, if, etc. 

El us de metodos, validaciones, etc. sirven mucho cuando quieres practicar sobre programación, 
te ayuda a entender un poco más la lógica de la programación.
"""

#Referencias
"""
- https://www.freecodecamp.org/espanol/news/metodos-de-string-de-python-explicados-con-ejemplo/
- https://www.w3schools.com/python/python_try_except.asp
- https://www.geeksforgeeks.org/python/isupper-islower-lower-upper-python-applications/
- https://www.w3schools.com/python/python_strings_slicing.asp
- https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/
"""