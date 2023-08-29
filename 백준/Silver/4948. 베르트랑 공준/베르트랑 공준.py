res = []
inf = 123456
num = [0]*((inf * 2) + 1)
num[0] = 1
for i in range(2,inf+1):
    if num[i]:
        continue
    for j in range(2,inf+1):
        if i*j > (inf*2):
            break
        num[i*j] = 1

while True:
    n = int(input())
    if not n:
        break
    cnt = 0

    for i in range(n+1,(2*n)+1):
        if not num[i]:
            cnt += 1

    res.append(cnt)

print(*res, sep='\n')