"""
Las tuplas son listas de elementos que no pueden 
cambiar su tamaño. Las tuplas son listas inmutables.

Se utilizan los () para definir una tupla.

Ejemplo:
"""
# Rectangulo (largo, ancho)
rectangle_dimansions = (200, 50)
print(f"largo:{rectangle_dimansions[0]}") # Imprime: largo:200
print(f"ancho:{rectangle_dimansions[1]}") # Imprime: ancho:50

# Vamos a inentar modificar una tupla
# rectangle_dimansions[0] = 250 # Error de tipo (TypeError)
# rectangle_dimansions[1] = 100 # Error de tipo (TypeError)

for dimension in rectangle_dimansions:
    print(dimension)

"""

"""

rectangle_dimansions = (300, 150) #Tupla
