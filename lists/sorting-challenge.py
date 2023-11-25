"""
🛠️ Coding example: Build a program that takes a list of names and sorts them alphabetically.

the original
["Marie Moreau", "Jordan Li", "Victoria Neuman", "Andre Anderson"]

the sorted
['Andre Anderson', 'Jordan Li', 'Marie Moreau', 'Victoria Neuman']

🧠 Teaser: How do you sort using not the first name, but the last name?
"""

names = ['Andre Anderson', 'Jordan Li', 'Marie Moreau', 'Victoria Neuman']
# dgasdgs = names[-4]
# print(dgasdgs)

# print(names[1:3])

print(f'Before: {names}')

names.sort()

print(f'After: {names}')
