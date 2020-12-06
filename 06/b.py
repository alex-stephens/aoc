answers = [[]]
with open('input.txt') as f:
    for line in f.readlines():
        if line.strip() == '':
            answers.append([])
        else: 
            answers[-1].append(line.strip())
        
def score(answer):
    score = 0
    n = len(answer)
    letters = {}
    for a in answer:
        for c in a:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1

    for c in letters.keys():
        if letters[c] == n:
            score += 1
    return score

print(sum([score(a) for a in answers]))