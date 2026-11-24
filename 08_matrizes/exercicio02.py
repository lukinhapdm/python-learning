"""
Exercício 2. Exibir a transposta de uma matriz 3x2.
"""
m = [[1, 2], [3, 4], [5, 6]]
t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
for linha in t:
    print(linha)
