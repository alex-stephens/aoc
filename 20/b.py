DEBUG = False

class Tile(object):
    def __init__(self, id, grid):

        self.id = id
        self.grid = grid

        # Clockwise directed edges
        self.T = grid[0]
        self.B = grid[-1][::-1]
        self.L = ''.join([r[0] for r in grid[::-1]])
        self.R = ''.join([r[-1] for r in grid])

        self.pos = None

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

        for i, r in enumerate(self.grid):
            self.grid[i] = r[::-1]

    # def flip_vertical(self):
    #     self.L = self.L[::-1]
    #     self.R = self.R[::-1]
    #     T, B = self.T, self.B
    #     self.T = B[::-1]
    #     self.B = T[::-1]

    def rotate_cw(self):
        T, B, L, R = self.T, self.B, self.L, self.R
        self.R = T
        self.B = R
        self.L = B
        self.T = L

        n = len(self.grid)
        gcopy = [x for x in self.grid]
        for i in range(n):
            self.grid[i] = ''.join([gcopy[j][i] for j in reversed(range(n))])

    # def rotate_ccw(self):
    #     T, B, L, R = self.T, self.B, self.L, self.R
    #     self.R = B
    #     self.B = L
    #     self.L = T
    #     self.T = R

class Grid(object): 
    def __init__(self):
        self.tiles = {}
        self.adj = {(0,0)}
        self.ids = set()

    def add_tile(self, t, pos):
        if pos in self.tiles:
            if DEBUG: print('Invalid: tile already exists--------------------------------')
            return False

        if self.try_insert_all(t, pos):
            if DEBUG: print('Inserted tile at', pos)
            return True
        if DEBUG: print('Insert failed')
        return False

        
    def try_insert_all(self, t, pos):
        
        for _ in range(4):
            if self.try_insert(t, pos):
                return True
            t.rotate_cw()
        t.flip_horizontal()
        for _ in range(4):
            if self.try_insert(t, pos):
                return True
            t.rotate_cw()

        return False

    def try_insert(self, t, pos):
        r, c = pos 

        # CHeck compatibility with 4 adjacent tiles
        if (r-1,c) in self.tiles: 
            if self.tiles[(r-1,c)].B != t.T[::-1]:
                return False     
        if (r,c-1) in self.tiles:
            if self.tiles[(r,c-1)].R != t.L[::-1]:
                return False
        if (r+1,c) in self.tiles: 
            if self.tiles[(r+1,c)].T != t.B[::-1]:
                return False     
        if (r,c+1) in self.tiles:
            if self.tiles[(r,c+1)].L != t.R[::-1]:
                return False

        # Insert
        self.tiles[(r,c)] = t
        self.ids.add(t.id)
        self.adj.remove(pos)
        if DEBUG: print('Removed tile from adj')
        adjs = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
        for a in adjs:
            if a not in self.tiles:
                self.adj.add(a)

        return True

    def build_image(self):
        rvals = [x[0] for x in self.tiles.keys()]
        cvals = [x[1] for x in self.tiles.keys()]
        rmin, rmax = min(rvals), max(rvals)
        cmin, cmax = min(cvals), max(cvals)

        if DEBUG: (rmin, rmax, cmin, cmax)
        rows, cols = rmax-rmin+1, cmax-cmin+1
        n = len(self.tiles[(0,0)].grid) - 2

        self.image = [['x' for _ in range(cols*n)] for _ in range(rows*n)]
        for r in range(rmin, rmax+1):
            for c in range(cmin, cmax+1):
                rs, cs = r*n, c*n
                for i in range(n):
                    for j in range(n):
                        self.image[rs+i][cs+j] = self.tiles[(r,c)].grid[i+1][j+1]
        
        for r in range(len(self.image)):
            self.image[r] = ''.join(self.image[r])

        if DEBUG: ('FULL GRID')
        if DEBUG: print(*self.image, sep='\n')

    def rotate_image_cw(self):
        n = len(self.image)
        imcopy = [x for x in self.image]
        for i in range(n):
            self.image[i] = ''.join([imcopy[j][i] for j in reversed(range(n))])

    def flip_image_horizontal(self):
        for i, r in enumerate(self.image):
            self.image[i] = r[::-1]

    def try_monsters_all(self, monster):
        rm, cm = len(monster), len(monster[0])

        for _ in range(4):
            count = self.match(monster)
            if count > 0:
                return count
            self.rotate_image_cw()
        self.flip_image_horizontal()

        for _ in range(4):
            count = self.match(monster)
            if count > 0:
                return count
            self.rotate_image_cw()

        return 0
        

    def match(self, monster):
        rm, cm = len(monster), len(monster[0])
        count = 0

        for r in range(len(self.image) - rm + 1):
            for c in range(len(self.image[0]) - cm + 1):
                found = True
                for i in range(rm):
                    for j in range(cm):
                        if monster[i][j] == '#' and self.image[r+i][c+j] != '#':
                            found = False
                            break
                    if not found: 
                        break
                if found: 
                    count += 1
        return count




        
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
posmap = {6:'corner', 7:'edge', 8:'interior'}
corners, edges, interiors = [], [], []

for t in tiles: 
    tot = 0
    sides = [t.T, t.B, t.L, t.R]
    for s in sides: 
        tot += occ[s]
    t.pos = posmap[tot]

    if t.pos == 'corner':
        corners.append(t)
    elif t.pos == 'edge':
        edges.append(t)
    else: 
        interiors.append(t)

grid = Grid()

# Top left corner at (0,0)
c0 = corners[0]
while True: 
    if occ[c0.L] == 1 and occ[c0.T] == 1:
        break
    c0.rotate_cw()

grid.add_tile(c0, (0,0))
if DEBUG: print('Successfully inserted first corner', c0.id)

while len(grid.tiles) < len(tiles):
    for t in tiles: 
        if t.id in grid.ids:
            continue
        adjset = set(grid.adj)
        for a in adjset:
            if grid.add_tile(t, a):
                break

grid.build_image()

monster = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']
msize = sum([s.count('#') for s in monster])
gcnt = sum([s.count('#') for s in grid.image])

count = grid.try_monsters_all(monster)
print(gcnt - msize*count)