import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())
heap = []
res = []
for _ in range(n):
    x = int(input())
    if not x:
        if heap:
            tmp = heappop(heap)
            res.append(tmp[1])
        else:
            res.append(0)
    else:
        heappush(heap,(-x,x))
print(*res, sep='\n')