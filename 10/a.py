p = []
with open('input.txt') as f:
    for line in f.readlines():
        p.append(int(line))
p = [0] + sorted(p) + [max(p) + 3]
n = len(p)
diffs = [0] * 4

for i in range(1,n):
    d = p[i] - p[i-1]
    diffs[d] += 1

print(diffs[1] * diffs[3])