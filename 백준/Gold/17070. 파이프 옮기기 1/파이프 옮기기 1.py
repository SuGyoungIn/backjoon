import sys
input = sys.stdin.readline

n = int(input())
pipe = [list(map(int,input().split())) for _ in range(n)]
dp = [list([0,0,0] for _ in range(n)) for _ in range(n)]

dp[0][1][0] += 1

for i in range(n):
    for j in range(n):
        if pipe[i][j] == 0:
            if 0<=i-1<n and 0<=j<n and pipe[i-1][j] == 0:
                dp[i][j][2] += dp[i-1][j][1] + dp[i-1][j][2]

            if 0<=i<n and 0<=j-1<n and pipe[i][j-1] == 0:
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][1]

            if 0<=i-1<n and 0<=j-1<n and pipe[i-1][j-1] == 0:
                if pipe[i][j-1] == 0 and pipe[i-1][j] == 0:
                    dp[i][j][1] += sum(dp[i-1][j-1])

print(sum(dp[n-1][n-1]))