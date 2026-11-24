"""
Exercício 3. Ler o salario e o percentual de aumento e exibir o novo salario.
"""
salario = float(input("Salario: "))
perc = float(input("Aumento (%): "))
print(f"Novo salario: R$ {salario * (1 + perc / 100):.2f}")
