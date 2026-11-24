"""
Exercício 1. Ler 5 notas, armazenar em lista e exibir a media e as notas acima da media.
"""
notas = []
for i in range(5):
    notas.append(float(input(f"Nota {i + 1}: ")))
media = sum(notas) / len(notas)
print(f"Media: {media:.2f}")
print("Acima da media:", [n for n in notas if n > media])
