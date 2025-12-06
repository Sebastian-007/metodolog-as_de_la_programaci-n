# Alumno: Gael Sebastian Castillo Salazar
# Matrícula: 2530240
# Grupo: IM 1-2

# Resumen Ejecutivo:
"""
Un CRUD (Create, Read, Update, Delete) es un conjunto de operaciones fundamentales para gestionar datos en memoria. 
"Create" crea un nuevo elemento, "Read" lee los datos de un elemento, "Update" modifica un elemento existente, 
y "Delete" elimina un elemento. En este programa, se eligió utilizar una lista de diccionarios para almacenar los elementos, 
donde cada diccionario representa un item. El uso de funciones para cada operación simplifica la lógica y organiza el código 
de manera eficiente. El programa incluye un menú interactivo para que el usuario realice operaciones CRUD sobre los items almacenados, 
con validaciones para asegurar la entrada correcta de datos.
"""

# Problema: Gestor CRUD usando diccionarios y/o listas con funciones.
"""
Description:
Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, 
por ejemplo, un producto de inventario con los siguientes campos sugeridos:

- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

El programa debe:

1) Definir una estructura de datos principal:
   - Opción A: dict item_id -> dict con datos del ítem.
   - Opción B: list de dicts, cada dict con campos id, name, price, quantity.
   (En comentarios, explica cuál opción escogiste y por qué.)

2) Definir FUNCIONES separadas para cada operación CRUD:
   - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
   - read_item(data_structure, item_id) -> dict o None
   - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
   - delete_item(data_structure, item_id) -> bool
   - list_items(data_structure) -> list o simplemente imprime
   Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

3) Implementar un MENÚ en el código principal (main loop):
   Ejemplo de opciones:
   - 1) Create item
   - 2) Read item by id
   - 3) Update item by id
   - 4) Delete item by id
   - 5) List all items
   - 0) Exit

4) En el bucle principal:
   - Mostrar el menú.
   - Leer la opción.
   - Según la opción, pedir los datos necesarios (id, name, price, quantity).
   - Llamar a la función correspondiente.
   - Mostrar mensajes claros de resultado.

Inputs:
- option (string o int; opción de menú).
- item_id (string o int).
- name (string).
- price (float).
- quantity (int).

Outputs:
- Mensajes tipo:
  - "Item created"
  - "Item updated"
  - "Item deleted"
  - "Item not found"
  - "Items list:" y luego la lista de elementos (formato libre pero legible).

Validations:
- option debe ser una de las opciones definidas (por ejemplo 0–5).
- item_id no vacío tras strip().
- price y quantity deben ser números válidos:
  - price >= 0.0
  - quantity >= 0
- Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
- En CREATE:
  - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
- En READ/UPDATE/DELETE:
  - Si el id no existe, mostrar "Item not found".

Requisitos de funciones:
- Cada operación CRUD debe estar encapsulada en al menos una función.
- El código del menú principal NO debe contener toda la lógica; debe delegar a las funciones.
- Las funciones deben tener nombres descriptivos y usar parámetros/return en lugar de depender de variables globales (en lo posible).

Sugerencia de flujo:
- Un while principal que corre hasta que el usuario elija 0 (Exit).
- Dentro del while:
  - Mostrar menú.
  - Leer opción.
  - if/elif para decidir qué función llamar.
- Probar el programa con varios casos antes de entregar.

Test cases:
1) Normal: 
Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Enter item id: 001
Enter item name: Producto 1
Enter item price: 21
Enter item quantity: 12
Item created

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Enter item id: 001
ID: 001, Name: Producto 1, Price: 21.0, Quantity: 12

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 3
Enter item id: 001
Enter new item name: Producto de prueba
Enter new item price: 50
Enter new item quantity: 30
Item updated

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 4
Enter item id: 001
Item deleted

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 0
Exiting...

2) Border: 

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Enter item id: 002
Enter item name: Caso a borde
Enter item price: 50
Enter item quantity: 0
Item created

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Enter item id: 002
ID: 002, Name: Caso a borde, Price: 50.0, Quantity: 0

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 0
Exiting...

3) Error: 
Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 6
Error: invalid option

Menu:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 0
Exiting...

"""

# Código
def create_item(data_structure, item_id, name, price, quantity):
    if item_id in [item['id'] for item in data_structure]:
        return "Item with this id already exists"
    item = {"id": item_id, "name": name, "price": price, "quantity": quantity}
    data_structure.append(item)
    return "Item created"

def read_item(data_structure, item_id):
    for item in data_structure:
        if item['id'] == item_id:
            return item
    return "Item not found"

def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    for item in data_structure:
        if item['id'] == item_id:
            item['name'] = new_name
            item['price'] = new_price
            item['quantity'] = new_quantity
            return "Item updated"
    return "Item not found"

def delete_item(data_structure, item_id):
    for item in data_structure:
        if item['id'] == item_id:
            data_structure.remove(item)
            return "Item deleted"
    return "Item not found"

def list_items(data_structure):
    if not data_structure:
        return "No items available"
    for item in data_structure:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

def main():
    items = []
    while True:
        print("\nMenu:")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")
        option = input("Choose an option: ")

        if option == '0':
            print("Exiting...")
            break
        elif option == '1':
            item_id = input("Enter item id: ")
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                print(create_item(items, item_id, name, price, quantity))
            except ValueError:
                print("Error: invalid input")
        elif option == '2':
            item_id = input("Enter item id: ")
            result = read_item(items, item_id)
            if isinstance(result, dict):
                print(f"ID: {result['id']}, Name: {result['name']}, Price: {result['price']}, Quantity: {result['quantity']}")
            else:
                print(result)
        elif option == '3':
            item_id = input("Enter item id: ")
            new_name = input("Enter new item name: ")
            try:
                new_price = float(input("Enter new item price: "))
                new_quantity = int(input("Enter new item quantity: "))
                print(update_item(items, item_id, new_name, new_price, new_quantity))
            except ValueError:
                print("Error: invalid input")
        elif option == '4':
            item_id = input("Enter item id: ")
            print(delete_item(items, item_id))
        elif option == '5':
            list_items(items)
        else:
            print("Error: invalid option")

if __name__ == "__main__":
    main()

# Conclusiones
"""
El uso de funciones para implementar el CRUD permitió organizar y modularizar el código, facilitando la reutilización
y el mantenimiento del mismo. La elección de una lista de diccionarios como estructura de datos resultó adecuada 
para almacenar los elementos de manera flexible. La validación de entradas fue esencial para evitar errores 
en las operaciones y garantizar que los datos sean correctos antes de realizar cualquier acción. Esta estructura 
básica de CRUD se puede extender fácilmente a un sistema más complejo, integrando bases de datos o almacenamiento persistente.
"""

# References
"""
1) https://share.google/SGCVfM9Ubi65WbGCo
2) https://share.google/19TRHXmx38PVuGeLK
3) https://share.google/rjGvXlYSQI5qn35Ga
4) https://share.google/WFizftyZGYTxioh6A
"""