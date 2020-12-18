lines = []
with open('input.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

def op(s, a, b):
    return a + b if s == '+' else a * b

def make_symb_list(line):
    symbols = list(''.join(line.split(' ')))
    for i, s in enumerate(symbols):
        if s.isnumeric():
            symbols[i] = int(s)
    return preprocess(symbols)

# Add extra brackets to enforce order of operations
def preprocess(symbols):
    i = len(symbols) - 2
    while i > 1:
        s = symbols[i]
        if s == '+': 
            j, p = i+1, 0
            while True:
                if j == len(symbols):
                    symbols.insert(j+1, ')')
                    break
                elif symbols[j] == '(':
                    p += 1
                elif symbols[j] == ')':
                    p -= 1
                if j == len(symbols) or (p == 0 and symbols[j] not in ('+', '*')):
                    symbols.insert(j+1, ')')
                    break
                j += 1

            j, p = i-1, 0
            while True:
                if j == -1:
                    if p != 0:
                        print('fucked')
                    symbols.insert(0, '(')
                    break

                if symbols[j] == '(':
                    p += 1
                elif symbols[j] == ')':
                    p -= 1
                if  p == 0 and symbols[j] not in ('+','*'):
                    symbols.insert(j, '(')
                    break
                j -= 1
        i -= 1
    return symbols

ans = 0

for line in lines: 
    stack, operator = [0], ['+']
    symbols = make_symb_list(line)

    for s in symbols:
        if type(s) == int:
            n = op(operator[-1], stack[-1], s)
            stack[-1] = n
        elif s == '(':
            stack.append(0)      
            operator.append('+')  
        elif s == ')':
            operator.pop()
            n = stack.pop()
            stack[-1] = op(operator[-1], n, stack[-1])
        elif s == '*' or s == '+':
            operator[-1] = s  

    ans += stack[0]

print(ans)