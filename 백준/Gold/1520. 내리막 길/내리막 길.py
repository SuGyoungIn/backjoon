import sys
input = sys.stdin.readline

m,n = map(int,input().split())
land = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
d = [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(i,j):
    if dp[i][j] >= 0:
        return dp[i][j]

    if i == m-1 and j == n-1:
        return 1

    dp[i][j] = 0
    for dx,dy in d:
        ni,nj = i+dx, j+dy
        if 0<=ni<m and 0<=nj<n and land[i][j] > land[ni][nj]:
            dp[i][j] += dfs(ni,nj)

    return dp[i][j]

dfs(0,0)

print(dp[0][0])