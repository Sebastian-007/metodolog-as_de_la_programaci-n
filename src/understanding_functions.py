"""
    Functions

    Las funciones son bloques de código diseñadas 
    para realizar una tarea en especifica.

    Cuando queremos realizar la tarea que se ha definido 
    en un a función, tebnemos que llemar el nombre de 
    la función responsable de esto.

    Definición de una función (Syntax)

    def name_of_functions(parameters):
        actions
"""

def greet_mauro():
    print("Hola Mauro, que gusto de verte!!!")

# Parametros
def greet(username, msj):
    print(f"Hola {username}, {msj}")

# Argumentos
greet_mauro()
greet("Gael", "tienes sueño?")

"""
     Vamos a hacer un programa que genere 
     el nombre completo de una persona.

     Vamos a pasarle primer nombre, el segundo
     y el apellido.

     La función debe generar el nombre completo 
     y regresarle
"""

def create_full_name(first_name, last_name, middle_name= ""):
    """
    Docstring - This function creates creates the fullname
    of a person given its three name.
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name


user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe tus apellidos: ").strip().lower()

# Argumentos posicionales -> Positional Arguments
print(create_full_name(
    user_first_name,  
    user_last_name,
    user_middle_name
    ))

# Argumentos Posicionales -> Positional Arguments
full_name = create_full_name(
    user_first_name, 
    user_last_name,
    user_middle_name
    )

print(full_name)

# Argumentos Clave -> Keyboard Arguments
full_name_key = create_full_name(
    last_name=user_last_name,
    first_name=user_first_name,
    middle_name=user_middle_name
)

# Parametros opcionales 
profe_falso = create_full_name(user_first_name, user_last_name, user_middle_name)
print(profe_falso)

