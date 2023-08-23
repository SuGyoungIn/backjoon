import sys
from collections import deque
sys.setrecursionlimit(10**6)

d = [[-1,0],[1,0],[0,-1],[0,1]]


def change_land(i,j,k,n):
    arr[i][j] = k
    for di,dj in d:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 1:
            arr[ni][nj] = k
            change_land(ni,nj,k,n)


def bridge(i, j, b, n):
    v = [[0]*n for _ in range(n)]
    deq = deque()
    v[i][j] = 1
    deq.append((i, j))
    while deq:
        p, q = deq.popleft()
        for di, dj in d:
            ni, nj = p+di, q+dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                if arr[ni][nj] != 0 and arr[ni][nj] != b:
                    return v[p][q] - 1
                deq.append((ni, nj))
                v[ni][nj] = v[p][q] + 1
    return 10000


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = []
bre = 0
k = 2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            change_land(i,j,k,n)
            k += 1


for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            s = 0
            for di, dj in d:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                    s = 1
                    break
            if s:
                ans = bridge(i,j,arr[i][j],n)
                if ans == 1:
                    res.append(1)
                    bre = 1
                    break
                res.append(ans)
    if bre:
        break

print(min(res))