num = []
with open('input.txt') as f:
    num = list(map(int, f.readline().split(',')))
memory = {}

for i, n in enumerate(num):
    if n not in memory:
        memory[n] = [i]
    else:
        memory[n].append(i)
    last = n

for i in range(len(num), 30000000):
    if len(memory[last]) == 1:
        nxt = 0
        memory[nxt].append(i)
    else:
        nxt = memory[last][-1] - memory[last][-2]
        if nxt not in memory:
            memory[nxt] = []
        memory[nxt].append(i)
    last = nxt

print(last) # takes ~30s
