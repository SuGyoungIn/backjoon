import sys
from heapq import heappop,heappush
input = sys.stdin.readline

V,E = map(int,input().split())
s = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


res = [3000001]*(V+1)
heap = []
heappush(heap,(0,s))
res[s] = 0
while heap:
    weight, now = heappop(heap)
    for point in graph[now]:
        v,w = point
        if res[v] > weight + w:
            res[v] = weight + w
            heappush(heap,(weight+w,v))

for i in range(1,V+1):
    if res[i] < 3000001:
        print(res[i])
    else:
        print('INF')