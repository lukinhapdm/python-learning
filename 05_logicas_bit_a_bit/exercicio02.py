"""
Exercício 2. Verificar se um numero e par usando operador bit a bit.
"""
n = int(input("Numero: "))
# o bit menos significativo e 0 nos pares
print("Par" if n & 1 == 0 else "Impar")
