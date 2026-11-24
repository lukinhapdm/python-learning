"""
Exercício 4. Multiplicar duas matrizes 2x2.
"""
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            c[i][j] += a[i][k] * b[k][j]
print(c)
