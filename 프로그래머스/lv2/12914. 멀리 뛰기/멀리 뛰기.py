
    
def solution(n):
    dp = [-1]*2001
    dp[1] = 1
    dp[2] = 2
    if not dp[n] == -1:
        return dp[n] % 1234567
    else:
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
    return dp[n] % 1234567