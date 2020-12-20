class Tile(object):
    def __init__(self, id, grid):

        self.id = id
        self.grid = grid

        # Clockwise directed edges
        self.T = grid[0]
        self.B = grid[-1][::-1]
        self.L = ''.join([r[0] for r in grid[::-1]])
        self.R = ''.join([r[-1] for r in grid])

    def display(self):
        print('-------------------------')
        print('Tile', self.id)
        print(*self.grid, sep='\n')
        print('-------------------------')

    def flip_horizontal(self):
        self.T = self.T[::-1]
        self.B = self.B[::-1]
        L, R = self.L, self.R
        self.L = R[::-1]
        self.R = L[::-1]

    def flip_vertical(self):
        self.L = self.L[::-1]
        self.R = self.R[::-1]
        T, B = self.T, self.B
        self.T = B[::-1]
        self.B = T[::-1]

    def rotate_cw(self):
        T, B, L, R = self.T, self.B, self.L, self.R
        self.R = T
        self.B = R
        self.L = B
        self.T = L

    def rotate_ccw(self):
        T, B, L, R = self.T, self.B, self.L, self.R
        self.R = B
        self.B = L
        self.L = T
        self.T = R
        
size = 10
tiles = []

with open('input.txt') as f:
    for line in f.readlines():
        if line.startswith('Tile'):
            id = int(line.split(' ')[1][:4])
            grid = []
        elif len(grid) < size:
            grid.append(line.strip())

        else:
            tiles.append(Tile(id, grid))
            # tiles[-1].display()
    tiles.append(Tile(id, grid))
    # tiles[-1].display()

occ = {}

for t in tiles: 
    sides = [t.T, t.B, t.L, t.R]
    sides += [t.T[::-1], t.B[::-1], t.L[::-1], t.R[::-1]]
    for s in sides: 
        if s in occ:
            occ[s] += 1
        else:
            occ[s] = 1

ans = 1

for t in tiles: 
    tot = 0
    sides = [t.T, t.B, t.L, t.R]
    # sides += [t.T[::-1], t.B[::-1], t.L[::-1], t.R[::-1]]
    for s in sides: 
        tot += occ[s]
    if tot == 6:
        ans *= t.id

print(ans)