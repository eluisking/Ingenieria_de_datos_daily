# Zip os sirve para emparejar listas(O cualquier iterable), basados en el ejemplo de abajo nos devolveria un tupla:
# Output: [('Thanos', 95), ('Dr. Doom', 98), ('Ultron', 90)]
villains = ["Thanos", "Dr. Doom", "Ultron"]
poderes = [95, 98, 90]

zipiando = zip(villains, poderes)
# Si queremos imprimirlos debemos convertir a otro iterable por ejemplo una lista.
print(list(zipiando))

# Emparejamos al vuelo dentro del for
for villano, poder in zip(villains, poderes):
    print(f"El villano {villano} tiene un nivel de poder de {poder}.")
# El villano Thanos tiene un nivel de poder de 95.
# El villano Dr. Doom tiene un nivel de poder de 98.
# El villano Ultron tiene un nivel de poder de 90.
