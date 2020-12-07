def parse(data):
    contents = {}
    bag, data = data.split(' bags contain ')
    data = data[:-1]

    if data == 'no other bags':
        return bag, contents

    for c in data.split(', '):
        qty = int(c.split(' ')[0])
        b = ' '.join(c.split(' ')[1:-1])
        contents[b] = qty

    return bag, contents

bag_to_contents = {}

with open('input.txt') as f:
    for line in f.readlines():
        data = line.strip()
        bag, contents = parse(data)
        bag_to_contents[bag] = contents

targets = [('shiny gold', 1)]
ans = 0

while len(targets) > 0:
    t, mult = targets.pop()

    for k in bag_to_contents[t].keys():
        ans += mult * bag_to_contents[t][k]
        targets.append((k, mult*bag_to_contents[t][k]))    

print(ans)


