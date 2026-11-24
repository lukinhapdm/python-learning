"""
Exemplo 2. Leitura de dados com input e conversao de tipos.
"""
nome = input("Nome: ")
# input sempre retorna str, por isso convertemos
idade = int(input("Idade: "))
print("Ola,", nome, "- ano que vem voce tera", idade + 1)
