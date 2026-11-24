"""
Exemplo 3. Expressao condicional (operador ternario) e match-case.
"""
n = int(input("Numero: "))
print("Par" if n % 2 == 0 else "Impar")

# match-case disponivel a partir do Python 3.10
dia = int(input("Dia da semana (1-3): "))
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terca")
    case _:
        print("Invalido")
