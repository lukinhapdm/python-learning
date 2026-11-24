"""
Exercício 1. Verificar se um ano e bissexto usando operadores logicos.
"""
ano = int(input("Ano: "))
# divisivel por 4 e nao por 100, ou divisivel por 400
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Bissexto")
else:
    print("Nao bissexto")
