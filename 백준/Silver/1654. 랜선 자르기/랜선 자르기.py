import sys
input = sys.stdin.readline

k,n = map(int,input().split())
cable = []
for _ in range(k):
    cable.append(int(input()))

l = 1
r = max(cable)
res = 0
while l <= r:
    m = (l + r)//2

    cnt = 0
    for i in range(k):
        cnt += cable[i]//m

    if cnt >= n:
        res = max(res,m)
        l = m+1
    else:
        r = m-1

print(res)