"""
Exercício 2. Inverter uma lista sem usar reverse nem fatiamento.
"""
lista = [1, 2, 3, 4, 5]
inv = []
# percorre do ultimo para o primeiro indice
for i in range(len(lista) - 1, -1, -1):
    inv.append(lista[i])
print(inv)
