import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

Log = 21
n = int(input())
tree = [[] for _ in range(n+1)]
rank = [0]*(n+1)
parents = [[0]*Log for _ in range(n+1)]
v = [0]*(n+1)
v[1] = 1
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(i,r):
    rank[i] = r
    for node in tree[i]:
        if v[node] == 0:
            v[i] = 1
            parents[node][0] = i
            dfs(node,r+1)

def findParent():
    dfs(1, 0)
    for i in range(1,Log):
        for j in range(1,n+1):
            parents[j][i] = parents[parents[j][i-1]][i-1]

def lca(a,b):
    if rank[a] > rank[b]:
        a,b = b,a
    for i in range(Log-1,-1,-1):
        if rank[b] - rank[a] >= (1 << i):
            b = parents[b][i]
    if a == b:
        return a
    for i in range(Log-1, -1,-1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]

    return parents[a][0]

findParent()

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))