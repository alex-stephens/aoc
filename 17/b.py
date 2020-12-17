init = []
with open('input.txt') as f:
    for line in f.readlines():
        init.append(line.strip())

cycles = 6
sx, sy = len(init[0]), len(init)
grid = {}

xlim, ylim, zlim, wlim = (sx+1)//2, (sy+1)//2, 0, 0
for i in range(sx):
    for j in range(sy):
        grid[(i - xlim, j - ylim, 0, 0)] = init[i][j]

def count_active(pos, lim):
    x, y, z, w = pos
    xl, yl, zl, wl = lim
    cnt = 0
    for i in range(-1,2):
        if x + i < -xl or x + i > xl: continue
        for j in range(-1,2):
            if y + j < -yl or y + j > yl: continue
            for k in range(-1,2):
                if z + k < -zl or z + k > zl: continue
                for m in range(-1,2):
                    if w + m < -wl or w + m > wl: continue
                    if (i, j, k, m) == (0, 0, 0, 0): continue
                    
                    if grid[(x+i,y+j,z+k,w+m)] == '#':
                        cnt += 1
    return cnt

for c in range(cycles):
    xlim, ylim, zlim, wlim = xlim+1, ylim+1, zlim+1, wlim+1
    lim = (xlim, ylim, zlim, wlim)
    grid_new = grid.copy()

    for x in range(-xlim, xlim+1):
        for y in range(-ylim, ylim+1):
            for z in range(-zlim, zlim+1):
                for w in range(-wlim, wlim+1):
                    if (x,y,z,w) not in grid:
                        grid[(x,y,z,w)] = '.'

    
    for x in range(-xlim, xlim+1):
        for y in range(-ylim, ylim+1):
            for z in range(-zlim, zlim+1):
                for w in range(-wlim, wlim+1):
                    pos = (x,y,z,w)
                    cnt = count_active(pos, lim)
                    active = True if grid[pos] == '#' else False
                    if active:
                        grid_new[pos] ='#' if (cnt == 2 or cnt == 3) else '.'
                    else:
                        grid_new[pos] = '#' if cnt == 3 else '.'
                
    grid = grid_new.copy()

print(list(grid.values()).count('#'))