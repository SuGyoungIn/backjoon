import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

def union(a,b):
    find_a = find(a)
    find_b = find(b)
    if find_a != find_b:
        parents[find_b] = find_a
        return True
    return False

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def dfs(i,j,s,cnt,dir):
    if maps[i][j] > 0:
        if maps[i][j] != s and cnt > 1:
            bridge[s][maps[i][j]] = min(bridge[s][maps[i][j]], cnt)
            return -1
        else:
            return 0

    ni,nj = i+d[dir][0], j+d[dir][1]
    if 0<=ni<n and 0<=nj<m:
        if maps[ni][nj] <= 0:
            maps[i][j] = dfs(ni,nj,s,cnt+1,dir)
        else:
            maps[i][j] = dfs(ni, nj, s, cnt, dir)
        return maps[i][j]
    else:
        return 0

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
parents = [i for i in range(8)]
# 섬 영역 유니크한 숫자로 바꾸기
q = deque()
cnt = 1
d = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            cnt += 1
            maps[i][j] = cnt
            q.append((i,j))

        while q:
            ni,nj = q.popleft()
            for di,dj in d:
                mi,mj = ni+di, nj+dj
                if 0<=mi<n and 0<=mj<m and maps[mi][mj] == 1:
                    maps[mi][mj] = cnt
                    q.append((mi,mj))



# 연결할 수 있는 다리 모두 만들기
bridge = [[100]*8 for _ in range(8)]
for i in range(n):
    for j in range(m):
        if maps[i][j] > 0:
            for k in range(4):
                ni,nj = i+d[k][0], j+d[k][1]
                if 0<=ni<n and 0<=nj<m and maps[ni][nj] <= 0:
                    dfs(ni,nj,maps[i][j],1,k)

# 다리 짦은 순으로 힙 원소 추가하기
heap = []
for i in range(2,8):
    for j in range(2,8):
        if bridge[i][j] < 100:
            heappush(heap,(bridge[i][j],i,j))

# 최소신장트리 만들기
res = 0
cntD = 0
while heap:
    length,a,b = heappop(heap)
    if union(a,b):
        res += length
        cntD += 1

if cntD == cnt - 2:
    print(res)
else:
    print(-1)