"""
Exercício 4. Calcular o fatorial de um numero.
"""
n = int(input("Numero: "))
fat = 1
for i in range(2, n + 1):
    fat *= i
print(f"{n}! = {fat}")
