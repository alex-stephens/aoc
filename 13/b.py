dep, buses = 0, []
with open('input.txt') as f:
    dep = int(f.readline())
    times = f.readline().split(',')

for i, t in enumerate(times): 
    if t != 'x':
        buses.append((i, int(t)))

base = buses[0][1]
n = len(buses)
keypoints = [[0,0] for _ in range(len(buses))]
diff = [0] * n

# Precomputation of modular arithmetic stuff
for i in range(len(buses)):
    t, n, cnt = 0, 0, 0
    while cnt < 2:
        if (t + buses[i][0]) % buses[i][1] == 0: 
            keypoints[i][cnt] = n
            cnt += 1
        t += base
        n += 1
    diff[i] = keypoints[i][1] - keypoints[i][0]

# Fast loop to find solution by multiplying base
t = 0
for i in range(len(buses)):
    while (t + buses[i][0]) % buses[i][1] != 0:
        t += base
    base *= diff[i]
print(t)