lines = []
with open('input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

cmds = {'ne':(0,1), 'nw':(-1,1), 'se':(1,-1), \
        'sw':(0,-1), 'e':(1,0),  'w':(-1,0)}
BLACK, WHITE = 1, 0
tiles = {} 

def move(pos, cmd):
    x, y = pos
    move = cmds[cmd]
    return (x + move[0], y + move[1])


def get_adj(pos):
    return [move(pos, c) for c in cmds.keys()]

def add_adj(pos):
    adj = get_adj(pos)
    for p in adj:
        if p not in tiles:
            tiles[p] = WHITE

def count_adj_black(pos):
    count = 0 
    for a in get_adj(pos):
        count += tiles[a] if a in tiles else 0
    return count


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
        tiles[pos] = 1
            
moves = 100
for i in range(moves):
    tiles_next = dict(tiles)

    for t in list(tiles.keys()):
        add_adj(t)
        
    for t in tiles:
        black = count_adj_black(t)

        if tiles[t] == BLACK and (black == 0 or black > 2):
            tiles_next[t] = WHITE

        elif tiles[t] == WHITE and black == 2:
            tiles_next[t] = BLACK

    tiles = dict(tiles_next)

print(sum(tiles.values()))
