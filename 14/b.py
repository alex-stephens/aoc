lines = []
with open('input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

mem = {}

def get_addresses(addr, mask):
    b = bin(addr)[2:]
    base = 0

    # Fixed bits
    for i, c in enumerate(reversed(mask)):
        if c == '0' and i < len(b):
            base += 2**i * int(b[-1-i])    
        elif c == '1':
            base += 2**i * int(c)

    # Floating bits
    addresses = [base]
    for i, c in enumerate(reversed(mask)):
        if c == 'X':
            delta = 2**i
            dup = [x + delta for x in addresses]
            addresses += dup
    
    return addresses

def write(val, addr, mask):
    addrs = get_addresses(addr, mask)
    for a in addrs:
        mem[a] = val

for line in lines:

    # Update mask
    if line.startswith('mask'):
        mask = list(line[7:])

    # Write result
    else:
        addr = int(line.split('[')[1].split(']')[0])
        val = int(line.split()[2])
        write(val, addr, mask)

print(sum([x for x in mem.values()]))