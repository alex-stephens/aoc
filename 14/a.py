lines = []
with open('input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

def apply_mask(val, mask):
    b = bin(val)[2:]
    result = 0
    for i, c in enumerate(reversed(mask)):
        if c == '0' or c == '1':
            result += 2**i * int(c)
        elif i < len(b): 
            result += 2**i * int(b[-1-i])

    return result

mem = {}

for line in lines:

    # Update mask
    if line.startswith('mask'):
        mask = list(line[7:])

    # Write result
    else:
        ind = int(line.split('[')[1].split(']')[0])
        val = int(line.split()[2])

        if ind not in mem: 
            mem[ind] = 0

        mem[ind] = apply_mask(val, mask)

print(sum([x for x in mem.values()]))