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
    if len(string) != lengths[r]:
        return False

    if type(rules[r]) == str: 
        return string == rules[r]

    for rule in rules[r]:
        parts = [lengths[x] for x in rule]
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
