import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(dp,sticker,i,j,n):
    if j == n - 1:
        return sticker[i][j]

    if not dp[i][j] == -1:
        return dp[i][j]

    tmp1, tmp2, tmp3 = 0, 0, 0
    if i == 0:
        tmp1 = func(dp, sticker, i+1, j+1,n)
        if j+2 < n:
            tmp2 = func(dp,sticker, i, j+2, n)
            tmp3 = func(dp, sticker, i+1,j+2, n)
        dp[i][j] = max(tmp1, tmp2, tmp3) + sticker[i][j]
    elif i == 1:
        tmp1 = func(dp, sticker, i - 1, j + 1, n)
        if j + 2 < n:
            tmp2 = func(dp, sticker, i, j + 2, n)
            tmp3 = func(dp, sticker, i - 1, j + 2, n)
        dp[i][j] = max(tmp1, tmp2, tmp3) + sticker[i][j]

    return dp[i][j]


T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[-1]*n for _ in range(2)]
    candi1 = func(dp,sticker,0,0,n)
    candi2 = func(dp,sticker,1,0,n)
    print(max(candi1,candi2))