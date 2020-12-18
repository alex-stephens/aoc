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