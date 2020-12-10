p = []
with open('input.txt') as f:
    for line in f.readlines():
        p.append(int(line))
p = [0] + sorted(p) + [max(p) + 3]
n = len(p)

# m[i] is the number of arrangements ending with p[i]
m = [1] + [0] * (n-1)

for i in range(1,n):
    for d in range(1,4):
        if i-d < 0:
            continue
        if p[i] - p[i-d] <= 3:
            m[i] += m[i-d]

print(m[-1])
        