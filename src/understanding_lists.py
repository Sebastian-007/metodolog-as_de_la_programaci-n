
# Listas
# Una lista es una colección ordenada y mutable de elementos.
# Se pueden crear listas utilizando corchetes y separando los elementos con comas.
fruits = ['manzana', 'banana','cereza']
print(fruits) # salida: ['manzana', 'banana','cereza']

# Acceso a elementos
print(fruits[0].upper()) # Salida de manzana
print(fruits[1].title()) # Salida de banana
print(fruits[2]) # Salida de cereza

# print(fruits[2]): # Esto generaría un error de indice fuera de rango

# Accede al ultimo elemento
print(fruits[-1])  # Salida de cereza
print(fruits[-2])  # Salida de banana
print(fruits[-3])  # Salida de manzana

message = f'Mi fruta favorita es {fruits[0].title()}.'
print(message) # Salida: Mi fruta favorita es Manzana

"""
   Agregar elementos a la lista
   - append(): Agrega un elemento al final de la lista.
"""
print ("\n Agregar elementos a una lista: Método append() \n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) 
motorcycles.append('ducati')
print(motorcycles)

"""
   Agregar elementos a una lista 
      - insert (): Inserta un elemento en una posicion especifica de la lista.
   El método inster(index, element) toma dos argumentos:
     el índice donde se desea insertar el elemento y el elemento en sí.
""" 
print ("\n Agregar elementos a una lista: Método insert() \n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
print(motorcycles[0])


"""
   Eliminar elemento de una lista: 
      - del: Elimina un elemento en una posición específica de la lista.
   La decclaracion del index elimina el elemento en la posición especificada.
"""
print ("\n Eliminar elementos de una lista: Declaración del \n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

"""
   Eliminar elemento de una lista: 
      - pop(): Elimina el último elemento de la lista y lo devuelve.
      El metodo pop() no requiere argumentos y elimina el último elemento de la lista.
"""
print ("\n Eliminar elementos de una lista: Método pop() \n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f'La motocicleta eliminada es: {popped_motorcycle}')

"""
   Eliminar elementos de una lista:
      - pop(index): Elimina y devuelve un elemento en una posición específica de la lista.
   El método pop(index) toma un argumento, que es el índice del elemento que se desea eliminar y devolver.
"""
print ("\n Eliminar elementos de una lista: Método pop(index) \n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(f'La primera motocicleta eliminada es: {first_motorcycle}')

"""
   Eliminar elementos de una lista:
      - remove(): Elimina la primera aparición de un valor específico en la lista.
   El método remove(value) toma un argumento, que es el valor del elemento que se desea eliminar.
"""
print ("\n Eliminar elementos de una lista: Método remove() \n")
motorcycles = ['honda','yamaha','suzuki','ducati','yamaha']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Ejemplo práctico del método remove()
names = ['ana','juan','pedro','maria', 'juan']
print(names)
deleted_name = input("\n \n Ingrse el nombre que desea eliminar de la lista: ")
names.remove(deleted_name.strip().lower())
print(names)