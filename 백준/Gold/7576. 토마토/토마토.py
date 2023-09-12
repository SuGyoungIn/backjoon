import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

d = [[0,1],[1,0],[0,-1],[-1,0]]

date = 0
q = deque()
v = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            v[i][j] = 1
            q.append((i,j,0))

while q:
    ni,nj,day = q.popleft()
    date = max(date,day)
    for di,dj in d:
        mi,mj = ni+di,nj+dj
        if 0<=mi<n and 0<=mj<m and v[mi][mj] == 0 and tomato[mi][mj] == 0:
            v[mi][mj] = 1
            tomato[mi][mj] = 1
            q.append((mi,mj,day+1))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            date = -1
            break

print(date)