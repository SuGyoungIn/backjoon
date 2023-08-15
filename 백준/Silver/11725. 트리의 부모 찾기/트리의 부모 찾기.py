import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
v = [0] * (n+1)
q.append(1)
v[1] = 1
while q:
    now = q.popleft()
    for node in tree[now]:
        if not v[node]:
            v[node] = now
            q.append(node)

for i in range(2,n+1):
    print(v[i])