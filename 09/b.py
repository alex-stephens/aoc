p = []
with open('input.txt') as f:
    for line in f.readlines():
        p.append(int(line))

def valid(p, t, n):
    sub = p[t-n:t]
    target = p[t]
    for i in range(n):
        for j in range(i+1,n):
            if sub[i] + sub[j] == target and sub[i] != sub[j]:
                return True
    return False

def check(p, preamble):
    for i in range(preamble, len(p)):
        if not valid(p, i, preamble):
            return p[i]
    return None

def weakness(p, target):
    n = len(p)

    # pc[i] is the sum of p[:i]
    pc = [p[0]] + [0] * (n-1) 
    for i in range(1,n):
        pc[i] = pc[i-1] + p[i]

    for i in range(n - 1):
        for j in range(i + 2, n):
            csum = pc[j-1] 
            csum -= pc[i-1] if i > 0 else 0
            if csum == target:
                return min(p[i:j]) + max(p[i:j])
    return -1

preamble = 25
target = check(p, preamble)
print(weakness(p, target))

