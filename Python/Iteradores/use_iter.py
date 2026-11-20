# En python podemos utilizar un blucle for para iterar elementos:
# Ejem:
supers = ["Capitan America", "Thor", "Hulk", "Wuanda"]

for super in supers:
    print(super)

# La otra forma es usar los iterbales e uteradores.
# Este es un iterable:
villains = ["Thanos", "Dr. Doom", "Ultron"]
# Aqui nuestra lista la hacemos un onbejeto iterador.
iterador = iter(villains)
# Para usar iter y revorrer los elementos usamos next; si usamos next mas que los elementos nos genera un error.
print(next(iterador))  # Thanos
print(next(iterador))  # Dr. Doom
print(next(iterador))  # Ultron
print(next(iterador))  # Este generara ERROR ya que solo tiene 3 elementos la lista.
