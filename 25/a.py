with open('input.txt') as f:
    key1, key2 = int(f.readline()), int(f.readline())

def transform(subject, loop, start=1):
    t = start
    for _ in range(loop):
        t = (t * subject) % 20201227
    return t

def find_loop_size(target):
    t = 7
    s = 1
    while t != target:
        t = transform(7, 1, t)
        s += 1
    return s

loop1 = find_loop_size(key1)
enc = transform(key2, loop1, 1)
print(enc)