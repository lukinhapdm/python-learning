"""
Exemplo 2. Metodos de lista: append, insert, remove, pop, sort.
"""
nums = [5, 2, 9]
nums.append(1)
nums.insert(0, 7)
nums.remove(9)
ultimo = nums.pop()
nums.sort()
print(nums, "removido:", ultimo)
print("Maior:", max(nums), "Soma:", sum(nums))
