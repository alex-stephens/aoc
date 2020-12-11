seats = []
with open('input.txt') as f:
    for line in f.readlines():
        seats.append(list(line.strip()))

rows, cols = len(seats), len(seats[0])

def display(seats):
    print('\n'.join([''.join(r) for r in seats]), end='\n\n')

def code(seats):
    return ''.join([''.join(r) for r in seats])

def valid(s):
    r, c = s
    return r >= 0 and r <= rows-1 and c >= 0 and c <= cols-1

def surroundings(r, c):

    dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    occ = 0

    for d in dirs: 
        s = (r,c)

        while True:
            s = (s[0]+d[0], s[1]+d[1])
            if not valid(s):
                break
            state = seats[s[0]][s[1]]
            if state == '#':
                occ += 1
            if state in ('#L'):
                break

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
            elif state == '#' and occ >= 5:
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



