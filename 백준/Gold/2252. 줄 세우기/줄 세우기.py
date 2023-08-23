import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
E = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    if E[a] == n+1:
        E[a] = 0
    if E[b] == n+1:
        E[b] = 0

    E[b] += 1
    graph[a].append(b)

q = deque()
res = []

for i in range(1, n+1):
    if E[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    res.append(now)
    if graph[now]:
        for node in graph[now]:
            E[node] -= 1
            if E[node] == 0:
                q.append(node)

print(*res)