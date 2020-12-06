answers = [[]]
with open('input.txt') as f:
    for line in f.readlines():
        if line.strip() == '':
            answers.append([])
        else: 
            answers[-1].append(line.strip())
        
def score(answer):
    score = 0
    letters = set()
    for a in answer:
        for c in a:
            if c not in letters:
                letters.add(c)
                score += 1
    return score

print(sum([score(a) for a in answers]))