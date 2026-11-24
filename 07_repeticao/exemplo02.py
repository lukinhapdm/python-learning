"""
Exemplo 2. Laco for com range e percorrendo listas.
"""
for i in range(0, 10, 2):  # inicio, fim (exclusivo), passo
    print(i, end=" ")
print()
for i, cor in enumerate(["azul", "verde"]):
    print(i, cor)
