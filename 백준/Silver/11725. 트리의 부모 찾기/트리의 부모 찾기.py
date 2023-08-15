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
q.append((0,1))
v[1] = 1
while q:
    parent,now = q.popleft()
    for node in tree[now]:
        if v[node] == 0:
            v[node] = now
            q.append((now,node))

for i in range(2,n+1):
    print(v[i])