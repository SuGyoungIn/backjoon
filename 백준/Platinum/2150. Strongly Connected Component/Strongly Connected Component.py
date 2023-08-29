import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
re_graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    re_graph[b].append(a)

stack = []
visited = [0] * (v+1)
re_visited = [0] * (v+1)

def dfs(i):
    visited[i] = 1

    for node in graph[i]:
        if not visited[node]:
            dfs(node)
    stack.append(i)

def re_dfs(i,scc):
    re_visited[i] = 1
    scc.append(i)

    for node in re_graph[i]:
        if not re_visited[node]:
            scc = re_dfs(node,scc)
    return scc

res = []
for i in range(1,v+1):
    if not visited[i]:
        dfs(i)

while stack:
    scc = []
    now = stack.pop()

    if re_visited[now]:
        continue
    res.append(sorted(re_dfs(now,scc)))


print(len(res))
for r in sorted(res):
    r.append(-1)
    print(*r)