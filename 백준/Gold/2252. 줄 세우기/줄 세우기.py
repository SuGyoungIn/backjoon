import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
E = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    E[b] += 1
    graph[a].append(b)

q = deque()
res = []

for i in range(1,n+1):
    if not E[i]:
        q.append(i)

while q:
    now = q.popleft()
    if graph[now]:
        for node in graph[now]:
            E[node] -= 1
            if not E[node]:
                q.append(node)

    res.append(now)

print(*res)