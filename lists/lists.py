sample_list = ["Marie", "Aba", 3, [1, 2, 4]]
print(sample_list)

sample_list.append(0)
sample_list.append(["Moreau", "A"])
print(sample_list)  

# 0        1     2      3      4          5  
['Marie', 'Aba', 3, [1, 2, 4], 0, ['Moreau', 'A']]
#  -6       -5   -4    -3      -2      -1

sample_list.pop()
print(sample_list)

print(sample_list.reverse())
print(sample_list)
