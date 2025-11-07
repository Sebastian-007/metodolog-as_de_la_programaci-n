"""
     Un string es de manera sencilla una serie de caracteres
     En python todo lo que se encuentre dentro de las comillas
       simples '' o comillas dobles "" es un string.

       "esto es un string"
       'Esto también es un string'

       'Le dije a un amigo, "¡Python es mi lenguaje favorito!"'
       "El lenguaje 'Python' lleva el nombre por Monty Python,
         no por la serpiente"

"""

name = "clase de programación"
print(name)
print(name.title())
print(name)


"""

Un método es una acción que python puede realizar
en un fragmento de datos o sobre una variable. 

El punto . después de una variable seguida del 
método title () dice que se tiene que ejecutar 
el método title() de la variable name.

Todods lo métodos van seguidos de paréntesis 
porque en ocasiones necesitan información adicional
para funcionar, lo cual iría dentro de los paréntesis.
En esta ocasión el método .title() no rrequiere 
información adicional para ejecutarse.

"""

print(name.upper())
print(name.lower())



# Concatenación de STRINGS
print("CONCATENACIÓN DE STRINGS")
first_name = "charly"
last_name = "mercury"
full_name = first_name + last_name 
print(full_name)
print("Hola, " + full_name.title() + "!")

# Syntax error con strings
message = "Una fortaleza de Python es su comunidad"
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message)


# Concatenación con f-strings
"""

() - parentesis
{} - laves
[] - corchete

"""
famous_person = "Gael castillo"
quote = "Python is love"

# Concatenación convencional
message = famous_person + " " + quote
print(message)

# Concatenación con f-strings
message_f_string = f"{famous_person} una ves dijo {quote}"
print(message_f_string)

# Actividad
"""
   1) Elige un personaje famoso e igualalo a una variable del tipo strings 
   2) Elige una frase famosa que haya dicho e iguala a una variable del tipo string
   3) Genera un mensaje con las dos variables utilizando f-strings
   4) Imprime el mensaje
"""

famous_person_2 = "Socrates"
quote_2 = "Solo se que no se nada"
message_f_string_2 = f"{famous_person_2} una ves dijo: {quote_2}"
print(message_f_string_2)

# Whitespaces
"""
Whitespaces se refiere a cualquier caracter que se imprime,
 es decir un tabulador y finales de línea. Los whitespaces
 se utilizan comunmente para organizar las salidas (prints)
 de tal manera que sea más amigable de leer o ver para los usuarios.

"""

# Ejemplos 
print("Python")
print("\tPython") # tabulador
print("\t\tPython") # doble tabulador

# Ejemplos Salto de linea
print("Languajes: \nPython \nC \nJavaScript")
print("Carlos")
print("Tovar")

message = """

    esta clase es de programación 

    mis compañeros son buena onda

                           metodologias de la programación
"""
print(message)


# Eliminacion de espacios en blanco 
programing_languages = " Python  JavaScript "
print(programing_languages)
print(programing_languages.lstrip()) # elimina espacios a la izquierda
print(programing_languages.rstrip()) # elimina espacios a la derecha
print(programing_languages.strip()) # elimina espacios a ambos lados