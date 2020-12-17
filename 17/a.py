init = []
with open('input.txt') as f:
    for line in f.readlines():
        init.append(line.strip())

cycles = 6
sx, sy, sz = len(init[0]), len(init), 1
grid = {}

xlim, ylim, zlim = (sx+1)//2, (sy+1)//2, 0
for i in range(sx):
    for j in range(sy):
        grid[(i - xlim, j - ylim, 0)] = init[i][j]

def count_active(pos, lim):
    x, y, z = pos
    xl, yl, zl = lim
    cnt = 0
    for i in range(-1,2):
        if x + i < -xl or x + i > xl: continue
        for j in range(-1,2):
            if y + j < -yl or y + j > yl: continue
            for k in range(-1,2):
                if z + k < -zl or z + k > zl: continue
                if (i, j, k) == (0, 0, 0): continue
                if grid[(x+i,y+j,z+k)] == '#':
                    cnt += 1
    return cnt

for c in range(cycles):
    xlim, ylim, zlim = xlim+1, ylim+1, zlim+1
    lim = (xlim, ylim, zlim)
    grid_new = grid.copy()

    for x in range(-xlim, xlim+1):
        for y in range(-ylim, ylim+1):
            for z in range(-zlim, zlim+1):
                if (x,y,z) not in grid:
                    grid[(x,y,z)] = '.'
    
    for x in range(-xlim, xlim+1):
        for y in range(-ylim, ylim+1):
            for z in range(-zlim, zlim+1):
                pos = (x,y,z)
                cnt = count_active(pos, lim)
                active = True if grid[pos] == '#' else False
                if active:
                    grid_new[pos] ='#' if (cnt == 2 or cnt == 3) else '.'
                else:
                    grid_new[pos] = '#' if cnt == 3 else '.'
                
    grid = grid_new.copy()

print(list(grid.values()).count('#'))