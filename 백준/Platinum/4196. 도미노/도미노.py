import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    global id
    stack.append(now)
    v[now] = id
    nowId = id
    for next in domino[now]:
        if not v[next]:
            id += 1
            dfs(next)
        if v[next] <= nowId:
            ind[next] -= 1
            v[now] = min(v[now],v[next])
    if v[now] == nowId:
        scc.append([])
        sccind.append(0)

        while True:
            a = stack.pop()
            scc[-1].append(a)
            sccind[-1] += ind[a]
            v[a] = 100000
            if a == now:
                break

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    domino = [[] for _ in range(n+1)]
    ind = [0] * (n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        domino[x].append(y)
        ind[y] += 1

    v = [0]*(n+1)
    stack,scc,sccind = [],[],[]
    for i in range(1,n+1):
        if not v[i]:
            id = 1
            dfs(i)
    print(sccind.count(0))