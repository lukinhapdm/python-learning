"""
Exemplo 3. Pertinencia com in e list comprehension.
"""
nums = [1, 2, 3, 4, 5]
print(3 in nums)
quadrados = [n ** 2 for n in nums]
pares = [n for n in nums if n % 2 == 0]
print(quadrados, pares)
