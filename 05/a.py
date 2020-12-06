# 1 for mandatory, 0 for optional
fields = {'byr':1, 'iyr':1, 'eyr':1, 'hgt':1, 'hcl':1, 'ecl':1, 'pid':1, 'cid':0}

seats = []
with open('input.txt') as f:
    for line in f.readlines():
        seats.append(line.strip())

def decode(seat):
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
    id = row*8 + col
    return (row, col, id)

print(max([decode(s)[2] for s in seats]))
