"""
Exercício 2. Ler numeros ate digitar 0 e exibir soma e quantidade.
"""
soma = cont = 0
while True:
    n = float(input("Numero (0 encerra): "))
    if n == 0:
        break
    soma += n
    cont += 1
print(f"Soma: {soma} | Quantidade: {cont}")
