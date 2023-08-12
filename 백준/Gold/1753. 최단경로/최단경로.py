import sys
from heapq import heappop,heappush
input = sys.stdin.readline

V,E = map(int,input().split())
s = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    if graph[u]:
        for i in range(len(graph[u])):
            v1,w1 = graph[u][i]
            if v1 == v:
                if w1 > w:
                    graph[u][i] = (v,w)
                break
        else:
            graph[u].append((v,w))
    else:
        graph[u].append((v,w))


res = [-1]*(V+1)
heap = []
heappush(heap,(0,s))
res[s] = 0
while heap:
    weight, now = heappop(heap)
    for point in graph[now]:
        v,w = point
        if res[v] == -1:
            res[v] = weight + w
            heappush(heap,(weight+w,v))
        elif res[v] > -1 and res[v] >= weight + w:
            res[v] = weight + w
            heappush(heap, (weight + w, v))

for i in range(1,V+1):
    if res[i] > -1:
        print(res[i])
    else:
        print('INF')