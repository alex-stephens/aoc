ingredients, allergens = [], []
all_allergens, all_ingredients = {}, {}
with open('input.txt') as f:
    for line in f.readlines():
        p1, p2 = line.strip().split('(')
        ingredients.append(set(p1.split()))
        allergens.append(set(p2[9:-1].split(', ')))
        for a in allergens[-1]:
            all_allergens[a] = ''
        for x in ingredients[-1]:
            all_ingredients[x] = ''

n = len(ingredients)

for a in all_allergens:
    occ = ''.join(['1' if a in allergens[i] else '0' for i in range(n)])
    all_allergens[a] = occ
for x in all_ingredients:
    occ = ''.join(['1' if x in ingredients[i] else '0' for i in range(n)])
    all_ingredients[x] = occ

def match(ingredient, allergen):
    for i in range(len(all_allergens[allergen])):
        if all_allergens[allergen][i] == '1' and \
            all_ingredients[ingredient][i] != '1':
            return False
    return True

candidates = {} # map ingredients to possible allergens

for x in all_ingredients:
    matched = False
    for a in all_allergens:
        if match(x, a):
            matched = True 
            if x in candidates:
                candidates[x].add(a)
            else:
                candidates[x] = set([a])

mapping = {}
total_pairs = len(all_allergens)

while len(mapping) < total_pairs:
    for x in candidates.keys():
        if len(candidates[x]) == 1:
            a = candidates[x].pop()
            mapping[x] = a
            break
    for x in candidates.keys():
        if a in candidates[x]:
            candidates[x].remove(a)

pairs = list([(x, mapping[x]) for x in mapping.keys()])
pairs.sort(key = lambda x: x[1])
ans = ','.join([x[0] for x in pairs])
print(ans)