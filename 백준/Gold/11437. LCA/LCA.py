import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
rank = [0]*(n+1)
parents = [0]*(n+1)
v = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(i,r):
    rank[i] = r
    for node in tree[i]:
        if not v[node]:
            v[i] = 1
            parents[node] = i
            dfs(node,r+1)

def lca(a,b):
    while rank[a] != rank[b]:
        if rank[a] > rank[b]:
            a = parents[a]
        else:
            b = parents[b]

    while a != b:
        a = parents[a]
        b = parents[b]
    return a

v[1] = 1
dfs(1,0)
res = []
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    res.append(lca(a,b))
print(*res, sep='\n')