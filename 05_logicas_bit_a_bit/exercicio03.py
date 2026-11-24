"""
Exercício 3. Ler um numero e exibir quantos bits 1 ele possui.
"""
n = int(input("Numero: "))
cont = 0
x = n
while x > 0:
    cont += x & 1  # soma o ultimo bit
    x >>= 1
print(f"{n} = {n:b} -> {cont} bits 1")
