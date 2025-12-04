# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

#Resumen Ejecutivo:
"""
Un bucle for es una estructura que se usa para repetir un bloque de código un número específico de veces, 
ideal cuando sabes cuántas veces necesitas iterar. Un bucle while, por otro lado, se usa cuando no sabes 
cuántas veces se debe repetir, y se ejecuta mientras se cumpla una condición específica. Un contador es 
una variable que lleva un registro de cuántas veces se ha ejecutado un bucle, mientras que un acumulador 
guarda un valor que se va actualizando en cada iteración. Es importante definir bien la condición de 
salida para evitar ciclos infinitos, que podrían hacer que el programa se quede atrapado sin terminar.

En mi documento, cubriré la descripción de cada problema, el diseño de entradas y salidas, las validaciones 
y el uso de bucles for y while. Utilicé for para recorrer rangos y hacer cálculos, y while para situaciones 
como menús interactivos o intentos repetidos hasta cumplir una condición. También me aseguré de validar 
las entradas antes de procesarlas.
"""

# Problem 1: Sum of range with for
"""
Description:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). Además, calcula la suma solo de los números 
pares en ese mismo rango usando un bucle for.

Inputs:
- n (int; límite superior del rango).

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validations:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de range(1, n + 1)
- Uso de un for con acumuladores para total_sum y even_sum.


Test cases:
1) Normal:
Enter the value of n: 5
Sum 1..5: 15
Even sum 1..5: 6

2) Border:
Enter the value of n: 1
Sum 1..1: 1
Even sum 1..1: 0

3) Error:
Enter the value of n: g
Error: invalid input

"""
# Código
n = input("Enter the value of n: ")
try:
    n = int(n)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print(f"Sum 1..{n}: {total_sum}")
        print(f"Even sum 1..{n}: {even_sum}")
except ValueError:
    print("Error: invalid input")


# Problem 2: Multiplication table with for
"""
Description:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Inputs:
- base (int)
- m (int; límite de la tabla)

Outputs:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validations:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, m + 1):
- Cálculo de producto y formateo de la salida con f-strings.

Test cases:
1) Normal:
Enter the base number: 3
Enter the limit m: 4
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12

2) Border:
Enter the base number: 2
Enter the limit m: 1
2 x 1 = 2

3) Error:
Enter the base number: x
Enter the limit m: 5
Error: invalid input

"""
# Código
base = input("Enter the base number: ")
m = input("Enter the limit m: ")

try:
    base = int(base)
    m = int(m)
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except ValueError:
    print("Error: invalid input")


# Problem 3: Average of numbers with while and sentinel
"""
Description:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.

Inputs:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Outputs:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validations:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

Operaciones clave sugeridas:
- while True con break al leer el sentinela o
- while number != sentinel_value
- Acumulador para suma y contador para cantidad.

Test cases:
1) Normal:
Enter a number (-1 to stop): 2
Enter a number (-1 to stop): 4
Enter a number (-1 to stop): 6
Enter a number (-1 to stop): -1
Count: 3
Average: 4.0

2) Border:
Enter a number (-1 to stop): 5
Enter a number (-1 to stop): -1
Count: 1
Average: 5.0

3) Error:
Enter a number (-1 to stop): -1
Error: no data

"""
# Código
sentinel_value = -1
count = 0
total_sum = 0

while True:
    number = input("Enter a number (-1 to stop): ")
    try:
        number = float(number)
        if number == sentinel_value:
            break
        total_sum += number
        count += 1
    except ValueError:
        print("Error: invalid input")

if count > 0:
    average = total_sum / count
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("Error: no data")


# Problem 4: Password attempts with while
"""
Descripción:
Implementa un sistema sencillo de intento de contraseña. Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. Si acierta dentro del límite, 
mostrar un mensaje de éxito. Si agota los intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

Operaciones clave sugeridas:
- while attempts < MAX_ATTEMPTS:
- Comparación de cadenas, contador de intentos.
- Opción de usar break al éxito.


Test cases:
1) Normal:
Enter password: admin123
Login success

2) Border:
Enter password: admin_123
Enter password: admin321
Enter password: admin123
Login success

3) Error:
Enter password: jajaja
Enter password: jajajaja
Enter password: jajajaja
Account locked

"""
# Código
MAX_ATTEMPTS = 3
correct_password = "admin123"
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")
    if user_password == correct_password:
        print("Login success")
        break
    else:
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# Problem 5: Simple menu with while
"""
Description:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.

Inputs:
- option (string o int; elección del usuario).

Outputs:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validations:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

Operaciones clave sugeridas:
- while option != 0:
- if/elif para cada opción.
- Variable counter inicializada fuera del bucle.

Test cases:
1) Normal:


2) Border:
Menú:
1) Mostrar saludo
2) Mostrar valor actual del contador
3) Incrementar contador
0) Salir
Elige una opción: 2
Contador: 0
Menú:
1) Mostrar saludo
2) Mostrar valor actual del contador
3) Incrementar contador
0) Salir
Elige una opción: 0
¡Adiós!

3) Error:
Menú:
1) Mostrar saludo
2) Mostrar valor actual del contador
3) Incrementar contador
0) Salir
Elige una opción: 5
Error: opción no válida
Menú:
1) Mostrar saludo
2) Mostrar valor actual del contador
3) Incrementar contador
0) Salir
Elige una opción: 0
¡Adiós!

"""
# Código
counter = 0

while True:
    print("Menu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    
    option = input("Choose an option: ")
    try:
        option = int(option)
        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")


# Problem 6: Pattern printing with nested loops
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. 
Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, n + 1):
    - construir una cadena con i asteriscos usando "*" * i
- (Opcional) otro bucle for para el patrón invertido.


Test cases:
1) Normal:
Enter the number of rows (n): 4
*
**
***
****

2) Border:
Enter the number of rows (n): 1
*

3) Error:
Enter the number of rows (n): 
Error: invalid input

"""
# Código
n = input("Enter the number of rows (n): ")
try:
    n = int(n)
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            print("*" * i)
        
except ValueError:
    print("Error: invalid input")




# Principios y buenas practicas
"""
- Usar for cuando conoces de antemano cuántas iteraciones necesitas (por ejemplo, 1 a 10).
- Usar while cuando la cantidad de iteraciones depende de una condición (por ejemplo, leer hasta que el usuario escriba "EXIT").
- Inicializar correctamente contadores y acumuladores antes del bucle.
- Actualizar las variables de control dentro del bucle while para no crear ciclos infinitos.
- Mantener el cuerpo del bucle lo más simple posible; extraer lógica compleja en funciones si es necesario.
"""

# Conclusiones
"""
Las diferencias prácticas entre usar for y while son claras: el for es ideal cuando conozco el número exacto de iteraciones, 
mientras que el while es útil cuando la condición es la que dicta el final del bucle. Los contadores y acumuladores fueron 
clave para llevar la cuenta de iteraciones y sumar valores dentro de los bucles. Un riesgo del while es generar ciclos 
infinitos si no se define correctamente la condición de salida. Los menús y los intentos de contraseña son ejemplos típicos 
de bucles while, ya que deben repetirse hasta que se cumpla una condición, como la entrada correcta. Además, aprendí sobre 
los bucles anidados y cómo se usan para generar patrones, como en el caso de los triángulos de asteriscos, lo que me permitió 
entender cómo gestionar la estructura de datos de forma más compleja.
"""

# Referencias
"""
- https://share.google/nKLqgcryxOMV9eZKl
- https://share.google/dSbOXpYxhmGyFQpIq
- https://share.google/vRObW0KzvfQrdqGov
- https://share.google/T2b0In71Eha5NbZr5
- https://share.google/53nVlug0MujfCzQ3j
"""