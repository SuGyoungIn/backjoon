import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = {}
for _ in range(n-1):
    a,b = map(int,input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

dp = [[0,0] for _ in range(n+1)]
v = [0]*(n+1)
def dfs(start):
    v[start] = 1
    for node in graph[start]:
        if v[node] == 0:
            dfs(node)
            dp[start][1] += min(dp[node][0], dp[node][1])
            dp[start][0] += dp[node][1]
    dp[start][1] += 1

dfs(1)
print(min(dp[1][0],dp[1][1]))