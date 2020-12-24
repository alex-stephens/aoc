lines = []
with open('input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

move_dir = {'ne':(0,1), 'nw':(-1,1), 'se':(1,-1), \
        'sw':(0,-1), 'e':(1,0),  'w':(-1,0)}
BLACK, WHITE = 1, 0
tiles = {}

def move(c, cmd):
    x, y = c
    move = move_dir[cmd]
    return (x + move[0], y + move[1])


for line in lines:
    pos = (0,0)
    i = 0
    while i < len(line):
        s = 2 if line[i] in 'ns' else 1
        cmd = line[i:i+s]
        pos = move(pos, cmd)
        i += s

    if pos in tiles:
        tiles[pos] = 1 - tiles[pos]
    else:
        tiles[pos] = BLACK
            
print(sum(tiles.values()))