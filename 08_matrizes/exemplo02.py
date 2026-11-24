"""
Exemplo 2. Criacao de matriz com list comprehension e leitura do usuario.
"""
lin, col = 2, 2
# evite [[0]*col]*lin: as linhas seriam a mesma referencia
m = [[0] * col for _ in range(lin)]
for i in range(lin):
    for j in range(col):
        m[i][j] = int(input(f"m[{i}][{j}]: "))
print(m)
