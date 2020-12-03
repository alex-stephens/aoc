grid = []
with open('input.txt') as f:
    for line in f.readlines():
        grid.append(line.strip())
rows, cols = len(grid), len(grid[0])

pos = [0,0] # row, col
slope = (3,1)
trees = 0 

while pos[0] < rows:
    if grid[pos[0]][pos[1] % cols] == '#':
        trees += 1

    pos[0] += slope[1]
    pos[1] += slope[0]

print(trees)