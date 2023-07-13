import sys
from collections import deque
input = sys.stdin.readline
d = [[0,1],[1,0],[0,-1],[-1,0]]
m,n,k = map(int, input().split())
rec = [list(map(int,input().split())) for _ in range(k)]
arr = [[0]*n for _ in range(m)]

def dfs(i,j,num):
    q = deque()
    cnt = 0
    q.append((i,j))
    arr[i][j] = num

    while q:
        cnt += 1
        di,dj = q.popleft()
        for dx, dy in d:
            ni, nj = di+dx, dj+dy
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] == 0:
                q.append((ni,nj))
                arr[ni][nj] = num

    return cnt


for r in rec:
    j1,i1,j2,i2 = r[0],r[1],r[2],r[3]

    for i in range(i1,i2):
        for j in range(j1,j2):
            arr[i][j] = 1

num = 2
res = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            res.append(dfs(i,j,num))
            num += 1

print(len(res))
res.sort()
print(*res)