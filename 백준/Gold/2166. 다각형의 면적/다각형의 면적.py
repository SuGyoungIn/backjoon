import sys
input = sys.stdin.readline

n = int(input())
coordinate = []
for _ in range(n):
    x,y = map(int,input().split())
    coordinate.append((x,y))

idx = 0
res1 = 0
res2 = 0
while idx < n:
    if idx == n-1:
        nextIdx = 0
    else:
        nextIdx = idx + 1
    x1,y1 = coordinate[idx]
    x2,y2 = coordinate[nextIdx]

    res1 += x1*y2
    res2 += y1*x2
    idx += 1

res = (res1-res2)/2
print(round(abs(res),2))