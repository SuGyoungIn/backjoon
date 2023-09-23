import sys
input = sys.stdin.readline
n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]
INF = 10**8
dp = [[-1]*(1<<n) for _ in range(n)]


def dfs(now,v):
    if v == (1 << n) - 1:
        if city[now][0]:
            return city[now][0]
        else:
            return INF

    if dp[now][v] != -1:
        return dp[now][v]

    tmp = INF
    for i in range(1,n):
        if v & (1 << i) != 0:
            continue
        if not city[now][i]:
            continue

        tmp = min(tmp, dfs(i, v | (1 << i)) + city[now][i])

    dp[now][v] = tmp

    return dp[now][v]

print(dfs(0,1<<0))