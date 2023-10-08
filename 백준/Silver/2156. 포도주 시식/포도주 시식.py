import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
elif n > 1:
    # 0: 이 잔이 첫번째일 경우
    # 1: 이 잔이 두번째일 경우
    # 2: 이 잔을 안마실 경우
    dp=[[0,0,0] for _ in range(n)]

    dp[0] = [arr[0],arr[0],0]
    dp[1] = [arr[1],dp[0][0]+arr[1],arr[0]]

    if n >= 3:
        for i in range(2,n):
            dp[i][0] = dp[i-1][2] + arr[i]
            dp[i][1] = dp[i-1][0] + arr[i]
            dp[i][2] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])

    print(max(dp[n-1]))
