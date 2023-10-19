import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def dfs(start,w):
    for next, d in tree[start]:
        if v[next] == -1:
            v[next] = w+d
            dfs(next,w+d)

v = [-1]*(n+1)
v[1] = 0
dfs(1,0)

start = v.index(max(v))
v = [-1]*(n+1)
v[start] = 0
dfs(start,0)
print(max(v))