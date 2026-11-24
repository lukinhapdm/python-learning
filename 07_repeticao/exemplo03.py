"""
Exemplo 3. break, continue e else em lacos.
"""
for n in range(1, 10):
    if n % 2 == 0:
        continue  # pula os pares
    if n > 7:
        break     # encerra o laco
    print(n)
else:
    print("Nao executa, pois houve break")
