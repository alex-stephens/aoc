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

err = 0
for nt in nearby:
    for n in nt: 
        valid = False
        for f in fields.keys():
            if satisfied(n, fields[f]):
                valid = True
                break
        if not valid: 
            err += n
print(err)



