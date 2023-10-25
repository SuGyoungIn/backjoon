n = int(input())
res = []
for _ in range(n // 4):
    res.append('long')

res.append('int')
print(*res, sep=" ")