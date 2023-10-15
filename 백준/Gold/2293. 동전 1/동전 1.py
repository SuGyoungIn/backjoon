import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
for _ in range(n):
    num = int(input())
    if num <= k:
        coin.append(num)

dp = [0]*(k+1)
dp[0] = 1
for c in coin:
    for i in range(c,k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])