p = []
with open('input.txt') as f:
    for line in f.readlines():
        p.append(line.strip())

def execute(p, i, acc, seen):
    cmd, val = p[i].split(' ')
    val = int(val)

    if cmd == 'nop':
        nexti = i + 1
    elif cmd == 'acc':
        acc += val
        nexti = i + 1
    elif cmd == 'jmp':
        nexti = i + val

    if nexti in seen: # infinite loop
        return -1, acc, seen
    elif nexti == len(p): # end
        return -2, acc, seen
    else:
        i = nexti
        seen.add(i)

    return i, acc, seen

def run(p):
    i = 0
    acc = 0
    seen = {0}

    while True: 
        inew, acc, seen = execute(p, i, acc, seen)
        if inew == -1:
            break
        elif inew == -2:
            break
        else:
            i = inew

    return acc, inew

swp = {'nop':'jmp', 'jmp':'nop'}

for i in range(len(p)):
    pcopy = list(p)
    if p[i][:3] in ('nop', 'jmp'):
        pcopy[i] = ''.join([swp[p[i][:3]], p[i][3:]])
    else:
        continue

    acc, status = run(pcopy)
    if status == -2:
        break

print(acc)