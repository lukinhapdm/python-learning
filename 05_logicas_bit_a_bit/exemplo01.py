"""
Exemplo 1. Operadores logicos and, or e not.
"""
idade = int(input("Idade: "))
tem_carteira = input("Tem carteira? (s/n): ") == "s"
# and: ambas verdadeiras
if idade >= 18 and tem_carteira:
    print("Pode dirigir")
# not inverte o valor logico
if not tem_carteira:
    print("Precisa tirar a carteira")
