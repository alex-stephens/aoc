grid = []
with open('input.txt') as f:
    for line in f.readlines():
        grid.append(line.strip())

rows, cols = len(grid), len(grid[0])
slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
ans = 1

for s in slopes:
    pos = [0,0] # row, col
    trees = 0 
    while pos[0] < rows:
        if grid[pos[0]][pos[1] % cols] == '#':
            trees += 1

        pos[0] += s[1]
        pos[1] += s[0]
    ans *= trees

print(ans)