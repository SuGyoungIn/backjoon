import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = int(input())

def dfs(start,visited,graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            res = dfs(v,visited,graph,-group)
            if not res:
                return False
        elif visited[v] == group:
            return False

    return True

for _ in range(k):
    v,e = map(int,input().split())
    visited = [0]*(v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i]:
            if not dfs(i,visited,graph,1):
                print("NO")
                break
    else:
        print("YES")