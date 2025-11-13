# List Comprehensions
"""
   Una list comprehension combina el for loop y la creación de nuevos 
   elementos en una sola línea de código y también, automáticamente 
   agrega el nuevo elemento a la lista, es decir, sin utilizar el append
"""

squares = [value**2 for value in range (1,11)]
print(squares)

# Números pares con el range
even_number_0_100_range = list(range(0,101,2))
print(even_number_0_100_range)

# Números pares utilizando list comprenhension
evens_list_compre = [value for value in range (0,101) if value%2 == 0]
print(evens_list_compre)
