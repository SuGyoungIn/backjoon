import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,R,Q = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [0]*(N+1)
v = [0]*(N+1)
def cntChild(i):
    if dp[i] > 0:
        return dp[i]

    for c in tree[i]:
        if v[c] == 0:
            v[c] = 1
            dp[i] += cntChild(c) +1

    return dp[i]

v[R] = 1
cntChild(R)

res = []
for _ in range(Q):
    a = int(input())
    res.append(dp[a]+1)

print(*res, sep="\n")