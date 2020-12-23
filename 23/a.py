class Circle(object):
    def __init__(self, string):

        vals = list(map(int, list(string)))
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
        if not final: 
            start = self.cur
            print(self.cur, end=' ')
        else:
            start = 1
        n = self.nxt[start]
        while n != start:
            print(n, end='')
            if not final: print(' ', end='')
            n = self.nxt[n]
        print()
        
    def move(self):
        extr = self.extract()
        dest = self.destination(extr)
        self.insert(dest, extr)

    def game(self, moves):
        for i in range(1,moves+1):
            self.move()

with open('input.txt') as f:
    for line in f.readlines():
        circle = Circle(line.strip())

m = 100
circle.game(m)
circle.print(1)