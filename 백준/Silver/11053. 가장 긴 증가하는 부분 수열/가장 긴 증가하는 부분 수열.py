n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n

dp[0] = 1

for i in range(1,n):
    cV = arr[i]
    maxV = 0
    for j in range(i):
        if arr[j] < cV:
            if maxV < dp[j]:
                maxV = dp[j]
    dp[i] = maxV + 1

print(max(dp))