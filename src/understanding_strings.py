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