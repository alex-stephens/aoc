num, ticket, nearby = [], [], [] 
fields = {}
with open('input.txt') as f:
    while True:
        line = f.readline().strip()
        if line == '':
            break
        field, constraints = line.split(': ')
        constraints = constraints.split(' or ')
        constraints = [(int(c.split('-')[0]), int(c.split('-')[1])) for c in constraints]
        fields[field] = constraints

    f.readline()
    ticket = list(map(int, f.readline().split(',')))
    f.readline()
    f.readline()

    while True:
        line = f.readline().strip()
        if line == '':
            break
        nt = list(map(int, line.split(',')))
        nearby.append(nt)

def satisfied(n, field):
    return (n >= field[0][0] and n <= field[0][1]) \
        or (n >= field[1][0] and n <= field[1][1])

# Eliminate invalid tickets
for i in reversed(range(len(nearby))):
    nt = nearby[i]
    for n in nt: 
        valid = False
        for f in fields.keys():
            if satisfied(n, fields[f]):
                valid = True
                break
        if not valid: 
            nearby.pop(i)

nearby.append(ticket)
nf = len(ticket)
possible_fields = [[] for _ in range(nf)]

# Compute valid fields for each index
for i in range(nf):
    for f in fields.keys():
        valid = True
        for n in nearby: 
            if not satisfied(n[i], fields[f]):
                valid = False
                break
        if valid: 
            possible_fields[i].append(f)

assigned_fields = ['' for _ in range(nf)]
fields_to_assign = list(fields.keys())
num_assigned = 0

# Eliminate invalid fields
while num_assigned < nf:
    cur = ''
    for i in range(nf):
        if len(possible_fields[i]) == 1:
            cur = possible_fields[i][0]
            break

    assigned_fields[i] = cur
    num_assigned += 1
    for i in range(nf):
        if cur in possible_fields[i]:
            possible_fields[i].remove(cur)

ans = 1
for f in fields.keys():
    if f.startswith('departure'):
        i = assigned_fields.index(f)
        ans *= ticket[i]
print(ans)







