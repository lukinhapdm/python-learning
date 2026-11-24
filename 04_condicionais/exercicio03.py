"""
Exercício 3. Calcular o IMC e exibir a classificacao.
"""
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / altura ** 2
if imc < 18.5:
    faixa = "Abaixo do peso"
elif imc < 25:
    faixa = "Normal"
elif imc < 30:
    faixa = "Sobrepeso"
else:
    faixa = "Obesidade"
print(f"IMC: {imc:.1f} - {faixa}")
