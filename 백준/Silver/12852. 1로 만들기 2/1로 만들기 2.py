n = int(input())

if n == 1:
    print(0)
    print(1)
else:
    dp = list([] for _ in range(n+1))
    dp[2] = [2,1]
    if n >= 3:
        dp[3] = [3,1]
        for i in range(4,n+1):
            dp[i].append(i)
            if i%3 == 0 and not i%2 == 0:
                if len(dp[i//3]) >= len(dp[i-1]):
                    dp[i] += dp[i-1]
                else:
                    dp[i] += dp[i//3]

            elif i%2 == 0 and not i%3 == 0:
                if len(dp[i//2]) >= len(dp[i-1]):
                    dp[i] += dp[i-1]
                else:
                    dp[i] += dp[i//2]
            elif i%3 == 0 and i%2 == 0:
                if len(dp[i//3]) <= len(dp[i//2]) and len(dp[i//3]) <= len(dp[i-1]):
                    dp[i] += dp[i//3]
                elif len(dp[i//2]) <= len(dp[i//3]) and len(dp[i//2]) <= len(dp[i-1]):
                    dp[i] += dp[i//2]
                elif len(dp[i-1]) <= len(dp[i//3]) and len(dp[i-1]) <= len(dp[i//2]):
                    dp[i] += dp[i-1]
            else:
                dp[i] += dp[i-1]

    print(len(dp[n]) - 1)
    print(*dp[n])