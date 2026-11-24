"""
Exercício 3. Ler uma matriz 3x3 e exibir a soma da diagonal principal.
"""
m = [[int(input(f"m[{i}][{j}]: ")) for j in range(3)] for i in range(3)]
# diagonal principal: i == j
print("Soma da diagonal:", sum(m[i][i] for i in range(3)))
