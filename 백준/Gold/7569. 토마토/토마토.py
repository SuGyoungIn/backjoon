import sys
from collections import deque

input = sys.stdin.readline
d = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
m,n,h = map(int,input().split())
tomato = list([list(map(int, input().split())) for _ in range(n)] for _ in range(h))

res = 0
def checkRipe():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    return False

    return True

allRipe = checkRipe()

if allRipe:
    print(0)
else:
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 1:
                    q.append((0,k,i,j))
    while q:
        date,nk,ni,nj= q.popleft()
        for dz,dx,dy in d:
            mk,mi,mj = nk+dz, ni+dx, nj+dy
            if 0<=mk<h and 0<=mi<n and 0<=mj<m:
                if tomato[mk][mi][mj] == 0:
                    q.append((date+1,mk,mi,mj))
                    res = date+1
                    tomato[mk][mi][mj] = 1


    if checkRipe():
        print(res)
    else:
        print(-1)