import sys
from heapq import heappush,heappop
input = sys.stdin.readline
inf = int(1e9)
def dijkstra(s):
    visited = [inf]*(n+1)
    q = []
    visited[s] = 0
    heappush(q,(0,s))

    while q:
        l,now = heappop(q)
        if visited[now] < l:
            continue
        else:
            for w,next in graph[now]:
                length = l+w
                if visited[next] > length:
                    visited[next] = length
                    heappush(q,(length,next))

    return visited

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1,v2 = map(int,input().split())
start1 = dijkstra(1)
startv1 = dijkstra(v1)
startv2 = dijkstra(v2)

pathv1 = start1[v1] + startv1[v2] + startv2[n]
pathv2 = start1[v2] + startv2[v1] + startv1[n]

res = min(pathv1,pathv2)
if res < inf:
    print(res)
else:
    print(-1)