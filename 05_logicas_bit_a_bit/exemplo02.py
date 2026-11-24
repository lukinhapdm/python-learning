"""
Exemplo 2. Operadores bit a bit: &, |, ^, ~, << e >>.
"""
a, b = 12, 10  # 1100 e 1010
print(f"a & b = {a & b} ({a & b:04b})")
print(f"a | b = {a | b} ({a | b:04b})")
print(f"a ^ b = {a ^ b} ({a ^ b:04b})")
print(f"~a = {~a}")
print(f"a << 1 = {a << 1}")  # multiplica por 2
print(f"a >> 2 = {a >> 2}")  # divide por 4
