"""
Exercício 3. Remover elementos duplicados mantendo a ordem.
"""
lista = [3, 1, 3, 2, 1, 5]
unicos = []
for x in lista:
    if x not in unicos:
        unicos.append(x)
print(unicos)
