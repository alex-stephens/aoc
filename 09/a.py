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

preamble = 25
print(check(p, preamble))