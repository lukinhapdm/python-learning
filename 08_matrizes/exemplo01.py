"""
Exemplo 1. Matriz como lista de listas e acesso aos elementos.
"""
m = [[1, 2, 3],
     [4, 5, 6]]
print(m[1][2])  # linha 1, coluna 2 -> 6
for linha in m:
    for valor in linha:
        print(f"{valor:3}", end="")
    print()
