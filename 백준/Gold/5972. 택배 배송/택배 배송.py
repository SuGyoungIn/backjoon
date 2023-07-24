import sys
import heapq
input = sys.stdin.readline
Inf = int(1e9)

n,m = map(int, input().split())
path = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    path[a].append((b,c))
    path[b].append((a,c))

distance = [Inf] * (n+1)

def dijkstra(start):
    q = []
    # 시작 노드의 거리는 0으로 설정
    distance[start] = 0
    heapq.heappush(q,(distance[start],start))
    while q:
        d,now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in path[now]:
            cost = d + i[1]
            if cost < distance[i[0]]: # 기존의 값보다 탐색한 길의 가중치가 적을 때
                distance[i[0]] = cost # 그 적은 값으로 갱신
                heapq.heappush(q,(cost, i[0]))

dijkstra(1)
print(distance[n])