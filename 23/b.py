class Circle(object):
    def __init__(self, string, size=None):

        vals = list(map(int, list(string)))
        if size:
            vals += [x for x in range(max(vals)+1, size+1)]

        self.nxt = {}
        self.n = len(vals)
        self.cur = vals[0]
        
        for i in range(len(vals)):
            self.nxt[vals[i]] = vals[(i+1) % self.n]

    def extract(self):
        c1 = self.nxt[self.cur]
        c2 = self.nxt[c1]
        c3 = self.nxt[c2]
        self.nxt[self.cur] = self.nxt[c3]
        return (c1, c2, c3)

    def destination(self, extr):
        t = self.cur - 1
        if t == 0: 
            t = self.n
        
        while t in extr: 
            t -= 1
            if t < 1:
                t = self.n
        return t

    def insert(self, dest, extr):
        c1, c2, c3 = extr
        n = self.nxt[dest]
        self.nxt[dest] = c1
        self.nxt[c3] = n
        self.cur = self.nxt[self.cur]

    def print(self, final=False):
        start = self.cur
        print(self.cur, end=' ')

        n = self.nxt[start]
        while n != start:
            print(n, end=' ')
            n = self.nxt[n]
        print()

    def move(self):
        extr = self.extract()
        dest = self.destination(extr)
        self.insert(dest, extr)

    def game(self, moves):
        step = 1000000
        for i in range(1,moves+1):
            self.move()
            if i % step == 0:
                print('Completed {} iterations'.format(i))

with open('input.txt') as f:
    line = f.readline()

size = 1000000
circle = Circle(line.strip(), size)

moves = 10000000
circle.game(moves)
ans = circle.nxt[1] * circle.nxt[circle.nxt[1]]
print(ans)