import sys
from collections import deque
input = sys.stdin.readline
d = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
def bfs(arr,cnt,i,j,w,h):
    q = deque()
    q.append((i,j))
    arr[i][j] = cnt

    while q:
        ni,nj = q.popleft()
        for di,dj in d:
            mi,mj = ni+di, nj+dj
            if 0<=mi<h and 0<=mj<w and arr[mi][mj] == 1:
                arr[mi][mj] = cnt
                q.append((mi,mj))

res = []
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int,input().split())) for _ in range(h)]
    cnt = 1
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                cnt += 1
                bfs(maps,cnt,i,j,w,h)

    res.append(cnt-1)

print(*res,sep="\n")