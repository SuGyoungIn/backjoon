import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n,m = map(int,input().split())
ind = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    ind[b] += 1

res = []
q = []

for i in range(1,n+1):
    if not ind[i]:
        heappush(q,i)

while q:
    now = heappop(q)
    if graph[now]:
        for p in graph[now]:
            ind[p] -= 1
            if not ind[p]:
                heappush(q,p)

    res.append(now)

print(*res)