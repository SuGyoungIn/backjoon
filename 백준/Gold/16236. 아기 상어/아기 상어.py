import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]
d=[[-1,0],[0,-1],[0,1],[1,0]]

def bfs(i,j,size):
    q = deque()
    v = [[0]*n for _ in range(n)]
    v[i][j] = 1
    q.append((0,i,j))
    candi = []
    while q:
        cnt,si,sj = q.popleft()
        if 0 < space[si][sj] < size:
            if len(candi) == 0:
                candi.append([cnt,si,sj])
            else:
                if candi[0][0] == cnt:
                    candi.append([cnt, si, sj])
        for di,dj in d:
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and space[ni][nj] <= size:
                v[ni][nj] = 1
                q.append((cnt+1,ni,nj))

    if candi:
        candi.sort(key=lambda x:(x[1],x[2]))
        return candi[0]
    else:
        return [0,i,j]

shark=(0,0)
flag = 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark = (i,j)
            flag = 1
            break
    if flag:
        break

space[shark[0]][shark[1]] = 0

eatCnt = 0
size = 2
res = 0
while True:
    sec,pi,pj = bfs(shark[0],shark[1],size)
    if sec:
        space[pi][pj] = 0
        res += sec
        eatCnt += 1
        shark = (pi, pj)
        if size == eatCnt:
            size += 1
            eatCnt = 0
    else:
        break

print(res)