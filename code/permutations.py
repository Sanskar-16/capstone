from itertools import permutations

dictA = {
    1: 19,
    2: 20,
    3: 99
}

perm = permutations(dictA.values())

for items in list(perm):
    print(items)