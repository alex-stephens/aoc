seats = []
with open('input.txt') as f:
    for line in f.readlines():
        seats.append(list(line.strip()))

# grid size
rows, cols = len(seats), len(seats[0])

def display(seats):
    print('\n'.join([''.join(r) for r in seats]), end='\n\n')

def code(seats):
    return ''.join([''.join(r) for r in seats])

def surroundings(r, c):
    rmin, rmax = max(r-1,0), min(r+1,rows-1)
    cmin, cmax = max(c-1,0), min(c+1,cols-1)

    occ = 0
    for i in range(rmin,rmax+1):
        for j in range(cmin,cmax+1):
            if (i,j) == (r,c):
                continue
            if seats[i][j] == '#':
                occ += 1

    return occ

it = 0
prevcode = ''

while True:
    it += 1
    new = [row[:] for row in seats]
          
    for i in range(rows):
        for j in range(cols):
            occ = surroundings(i, j)

            state = seats[i][j]
            if state == 'L' and occ == 0:
                new[i][j] = '#'
            elif state == '#' and occ >= 4:
                new[i][j] = 'L'
            else:
                new[i][j] = state

    seats = [row[:] for row in new]
    s = code(seats)
    if s == prevcode:
        break
    prevcode = s

print('Finished after {} iterations'.format(it))
print(prevcode.count('#'))



