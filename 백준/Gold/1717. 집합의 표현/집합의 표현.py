import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def find(c):
    if c != parent[c]:
        parent[c] = find(parent[c])
    return parent[c]

res = []
for _ in range(m):
    calc,a,b = map(int,input().split())
    if not calc:
        union(a,b)
    else:
        if find(a) == find(b):
            res.append('YES')
        else:
            res.append('NO')

print(*res, sep='\n')