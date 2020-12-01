num = [] 
with open('input.txt') as f:
    for x in f.readlines():
        num.append(int(x))

n = len(num)
t = 2020
ans = None
done = False

for i in range(n):
    for j in range(i+1,n):
        if num[i] + num[j] == t:
            ans = num[i] * num[j]
            done = True
            break
    if done:
        break

print(ans)