import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

sushi = []
for _ in range(n):
    sushi.append(int(input()))

answer = 0

for i in range(n):
    if sushi[i] == c:
        continue
    res = 0
    candi = []

    if i+k < n:
        candi = sushi[i:i+k]
    else:
        candi = sushi[i:n] + sushi[:i+k-n]

    arr = list(set(candi))
    res = len(arr)
    if c not in arr:
        res += 1

    if answer < res:
        answer = res

    if answer > k:
        break

print(answer)