"""
Las listas también pueden almacenar números y de echo son ideales para almacenarlos.
Python ofrece cantidad de funciones y métodos para trabajar con listas de números.

Por ejemplo, función range():

"""

# La función range() genera una lista de números.
# en un rango específico.
# Por ejemplo, para generar una lista de números del 0 al 9:
numeros = list(range(10))
print(numeros)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)

print("\nNúmeros del 1 al 4:")
for num in range(1, 5):
    print(num)
numbers_1_to_4 = list(range(1, 5))
print(numbers_1_to_4)  # Salida: [1, 2, 3, 4]

print("\nNúmeros impares:")
for num in range(1, 10, 2): # Números impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)  # Salida: [1, 3, 5, 7, 9]

print("\nNúmeros pares:")
for num in range(2, 10, 2): # Números impares del 1 al 9
    print(num)
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # Salida: [2, 4, 6, 8, 10]

# Podemos crear cualquier tipo de listas de números
# Utilizando range() y list()
print("\n Primeros 10 números al cuadrado: ")
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Métodos built-in para listas de números
print("\n Métodos built-in para listas de números:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Lista de dígitos:", digits)
print("Valor mínimo:", min(digits))  # Salida: 0
print("Valor máximo:", max(digits))  # Salida: 9
print("Suma de todos los valores:", sum(digits))  # Salida: 45