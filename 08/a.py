p = []
with open('input.txt') as f:
    for line in f.readlines():
        p.append(line.strip())

i = 0
acc = 0
seen = {0}

def execute(i, acc):
    cmd, val = p[i].split(' ')
    val = int(val)

    if cmd == 'nop':
        nexti = i + 1
    elif cmd == 'acc':
        acc += val
        nexti = i + 1
    elif cmd == 'jmp':
        nexti = i + val

    if nexti in seen:
        return -1, acc
    else:
        i = nexti
        seen.add(i)

    return i, acc

while True: 
    ret, acc = execute(i, acc)
    if ret == -1:
        break
    else:
        i = ret

print(acc)