import sys
from heapq import heappop,heappush
input = sys.stdin.readline

V,E = map(int,input().split())
graph = []
parents=[i for i in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    heappush(graph,(c,a,b))

def union(a,b):
    A = find(a)
    B = find(b)
    if A < B:
        parents[B] = A
        return True
    elif B < A:
        parents[A] = B
        return True
    else:
        return False

def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]

cnt = 0
res = 0
while graph and cnt < V:
    w,now,next = heappop(graph)
    if union(now,next):
        cnt += 1
        res += w
    else:
        continue

print(res)