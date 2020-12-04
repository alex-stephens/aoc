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
for i, p in enumerate(passports):
    invalid = False
    for f in fields.keys():
        if fields[f] == 1 and f not in passports[i]:
            invalid = True
            break
    if not invalid:
        valid += 1
print(valid)

