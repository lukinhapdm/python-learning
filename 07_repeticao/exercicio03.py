"""
Exercício 3. Verificar se um numero e primo.
"""
n = int(input("Numero: "))
primo = n > 1
# basta testar divisores ate a raiz quadrada
for d in range(2, int(n ** 0.5) + 1):
    if n % d == 0:
        primo = False
        break
print("Primo" if primo else "Nao primo")
