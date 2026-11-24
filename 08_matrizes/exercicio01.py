"""
Exercício 1. Somar duas matrizes 2x3.
"""
a = [[1, 2, 3], [4, 5, 6]]
b = [[6, 5, 4], [3, 2, 1]]
c = [[a[i][j] + b[i][j] for j in range(3)] for i in range(2)]
for linha in c:
    print(linha)
