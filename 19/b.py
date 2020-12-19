rules = {}
unresolved = {}
deps, resolved = {}, set()
msgs = []
lengths = {}

with open('input.txt') as f:
    for line in f.readlines():
        if line.find(':') > 0:
            n, r = line.strip().split(': ')
            n = int(n)

            if r.startswith("\""):
                rules[n] = r[1]
                resolved.add(n)
                lengths[n] = 1
            else: 
                r = r.split(' ')
                unresolved[n] = []
                deps[n] = set()
                i, cur = 0, []
                for j, c in enumerate(r):
                    if c == '|':
                        unresolved[n].append(tuple(cur))
                        cur = []
                        i += 1
                    else:
                        cur.append(int(c))
                        deps[n].add(int(c))
                unresolved[n].append(tuple(cur))

        elif line.strip() != '':
            msgs.append(line.strip())


rules = {**rules, **unresolved}
depth = 10

while len(unresolved) > 0:
    keys = list(unresolved.keys())
    for n in keys:
        resolvable = all([v in resolved for v in deps[n]])

        # Resolve the rule
        if resolvable:
            rule = unresolved.pop(n)
            lengths[n] = sum([lengths[v] for v in rule[0]])
            resolved.add(n)

def match(string, r):
    if r == 8 and len(string) > lengths[r]:
        L = lengths[42]
        return match(string[:L],42) and match(string[L:], 8)
    if r == 11 and len(string) > lengths[r]:
        L1, L2 = lengths[42], lengths[31]
        return match(string[:L1],42) and match(string[L1:-L2],11) and match(string[-L2:],31)

    # Base case
    if type(rules[r]) == str: 
        return string == rules[r]

    for rule in rules[r]:
        extended = [[lengths[x] for x in rule]]

        if 8 in rule and 11 in rule: 
            for d1 in range(1, depth+1): 
                for d2 in range(1, depth+1): 
                    if (d1, d2) == (1,1): continue
                    parts = [lengths[x] for x in rule]
                    i1, i2 = rule.index(8), rule.index(11)
                    parts[i1] = d1 * lengths[8]
                    parts[i2] = d2 * lengths[11]
                    extended.append(parts)

        for parts in extended:
            if sum(parts) != len(string):
                continue
            matched = True
            s = 0
            for i, p in enumerate(parts):
                if not match(string[s:s+p], rule[i]):
                    matched = False
                    break
                s += p
            if matched:
                return True
    return False

ans = sum([1 if match(m,0) else 0 for m in msgs])
print(ans)