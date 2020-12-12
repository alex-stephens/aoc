actions = []
with open('input.txt') as f:
    for line in f.readlines():
        actions.append(line.strip())

dirs = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
p = (0,0) # current position
h = (1,0) # current heading

for a in actions:
    c, val = a[0], int(a[1:])

    # Direction update
    if c in ('L,R'):
        if a in ('L90', 'R270'):
            h = (-h[1], h[0])
        elif a in ('R90', 'L270'):
            h = (h[1], -h[0])
        elif a in ('L180', 'R180'):
            h = (-h[0], -h[1])
        continue

    if c == 'F':
        p = (p[0] + h[0] * val, p[1] + h[1] * val)
    else: # NESW
        b = dirs[c] # bearing
        p = (p[0] + b[0] * val, p[1] + b[1] * val)
    
print(sum([abs(x) for x in p]))