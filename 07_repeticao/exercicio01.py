"""
Exercício 1. Exibir a tabuada de um numero lido.
"""
n = int(input("Numero: "))
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")
