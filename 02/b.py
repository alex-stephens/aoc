pol, pw = [], []
with open('input.txt') as f:
    for line in f.readlines():
        a, b = line.split(': ')
        pol.append(a)
        pw.append(b)

def read_policy(pol):
    n1 = int(pol.split('-')[0])
    n2 = int(pol.split('-')[1].split(' ')[0])
    letter = pol.split(' ')[1]
    return n1, n2, letter

valid = 0

for i in range(len(pol)):
    n1, n2, letter = read_policy(pol[i])

    if (pw[i][n1-1] == letter) ^ (pw[i][n2-1] == letter):
        valid += 1

print(valid)