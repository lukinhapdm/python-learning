"""
Exercício 1. Verificar se funcionario e bem ou mal remunerado (limite R$5.000,00). Fazer teste de mesa.
"""
salario = float(input("Salario: "))
# acima de 5000 e considerado bem remunerado
if salario > 5000:
    print("Bem remunerado")
else:
    print("Mal remunerado")
