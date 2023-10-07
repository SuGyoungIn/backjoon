n = int(input())
res = 0
for m in range(n):
    arr = list(str(m))
    tmp = m
    for i in arr:
        tmp += int(i)

    if tmp == n:
        res = m
        break

print(res)