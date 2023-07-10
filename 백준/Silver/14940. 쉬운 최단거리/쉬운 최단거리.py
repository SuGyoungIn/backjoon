import sys
from collections import deque
input = sys.stdin.readline
d = [[-1,0],[0,1],[1,0],[0,-1]]

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lenArr = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(i,j):
    visited[i][j] = 1
    q = deque()
    q.append((0,i,j))

    while q:
        nd, ni, nj = q.popleft()
        for dx,dy in d:
            mi,mj = ni+dx, nj+dy
            if 0<=mi<n and 0<=mj<m and arr[mi][mj] != 0 and visited[mi][mj] == 0:
                visited[mi][mj] = 1
                lenArr[mi][mj] = nd+1
                q.append((nd+1,mi,mj))
    return

flag = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i,j)
            flag = 1
            break
    if flag == 1:
        break


for i in range(n):
    for j in range(m):
        if lenArr[i][j] == 0:
            if arr[i][j] != 0 and arr[i][j] != 2:
                lenArr[i][j] = -1
    print(*lenArr[i])