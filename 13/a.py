dep, buses = 0, []
with open('input.txt') as f:
    dep = int(f.readline())
    times = f.readline().split(',')

for t in times: 
    if t != 'x':
        buses.append(int(t))

bus_id = 0
wait = 10000000

for b in buses: 
    w = b - (dep % b) 
    if w < wait: 
        wait = w
        bus_id = b

print(wait * bus_id)