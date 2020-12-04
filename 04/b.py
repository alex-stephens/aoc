# 1 for mandatory, 0 for optional
fields = {'byr':1, 'iyr':1, 'eyr':1, 'hgt':1, 'hcl':1, 'ecl':1, 'pid':1, 'cid':0}

passports = [{}]
with open('input.txt') as f:
    for line in f.readlines():
        if line.strip() == '':
            passports.append({})
            continue
        for field in line.strip().split():
            f, d = field.split(':')
            passports[-1][f] = d

valid = 0 

def in_range(val, lower, upper):
    return val >= lower and val <= upper

for i, p in enumerate(passports):
    invalid = False
    for f in fields.keys():
        if fields[f] == 1 and f not in passports[i]:
            invalid = True

    for f in fields.keys():
        if invalid: 
            break

        if f == 'byr': 
            if len(p[f]) != 4 or not in_range(int(p[f]), 1920, 2002):
                invalid = True
        if f == 'iyr': 
            if len(p[f]) != 4 or not in_range(int(p[f]), 2010, 2020):
                invalid = True
        if f == 'eyr': 
            if len(p[f]) != 4 or not in_range(int(p[f]), 2020, 2030):
                invalid = True
        if f == 'hgt': 
            if not p[f][-2:] in ('cm', 'in'):
                invalid = True
            elif p[f][-2:] == 'cm' and not in_range(int(p[f][:-2]), 150, 193):
                invalid = True
            elif p[f][-2:] == 'in' and not in_range(int(p[f][:-2]), 59, 76):
                invalid = True
        if f == 'hcl': 
            if p[f][0] != '#' or len(p[f]) != 7 or not p[f][1:].isalnum():
                invalid = True
        if f == 'ecl': 
            if p[f] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                invalid = True
        if f == 'pid': 
            if len(p[f]) != 9 or not p[f].isnumeric():
                invalid = True

    if not invalid:
        valid += 1
print(valid)

