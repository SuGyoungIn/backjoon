import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
Log = 21
tree = [[] for _ in range(n+1)]
depth = [0] * (n+1)
depth[1] = 1
dp = [[[0,0,0] for _ in range(Log)] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

q = deque([(1,1)])

while q:
    now, d = q.popleft()
    for next, w in tree[now]:
        if not depth[next]:
            q.append((next, d + 1))
            depth[next] = d + 1
            dp[next][0] = [now,w,w]

#최소 공통 조상 찾기
for j in range(1, Log):
    for i in range(1, n + 1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = min(dp[i][j-1][1], dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][2] = max(dp[i][j-1][2], dp[dp[i][j-1][0]][j-1][2])

k = int(input())
for _ in range(k):
    d,e = map(int,input().split())
    maxV = 0
    minV = float('inf')

    if depth[d] > depth[e]:
        d,e = e,d
    for i in range(Log-1,-1,-1):
        if depth[e] - depth[d] >= (1<<i):
            minV = min(dp[e][i][1], minV)
            maxV = max(dp[e][i][2], maxV)
            e = dp[e][i][0]

    if d == e:
        print(minV,maxV)
        continue

    for i in range(Log-2,-1,-1):
        if dp[d][i][0] != dp[e][i][0]:
            minV = min(dp[d][i][1], dp[e][i][1], minV)
            maxV = max(dp[d][i][2], dp[e][i][2], maxV)
            d = dp[d][i][0]
            e = dp[e][i][0]

    minV = min(dp[d][0][1], dp[e][0][1], minV)
    maxV = max(dp[d][0][2], dp[e][0][2], maxV)
    print(minV,maxV)