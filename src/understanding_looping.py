magicians = ["ron", "harry", "snope", "hermione"]

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()}: ese fue un gran hechizo.")
    print("\n")

print("Gracias a todos por participar en el espectáculo de hoy.")

"""
    Identación.
    
        Python utiliza la identación para determinar cuando era línea
        de código está conectada a la ínea de código anterior.

        Básicamente, se utliza 4 espacios en blanco para obligarnos
        a escribir código ordenado y estructurado.
"""

# No olvidemos identar (donde se necesita)
# Ejemplo
magicians = ["alice", "david", "jorge"]
for magician in magicians:
# print(magician) #Error de identación
    print(magician) # Correcto


# Identation error
# Logical error (error logico mio)
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
# print(f"Great {magician}!, I can't wait to see your next trick.")
    print(f"Great {magician}!, I can't wait to see your next trick.")

# Identación innecesaria
message = "Hola charly"
# print(message) # Error de identación innecesaria

# Logical error (error logico mio)
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I can't wait to see your next trick.")
print("thank you everyone, that was a great magic show!") # Solución (identar a la izquieda)

# Error de syntaxis
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians: # (SyntaxisError): olvidar colocar los dos puntos (:)
    print(magician)