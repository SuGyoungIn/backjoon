import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n-1,-1,-1):
    if coin[i] <= k:
        tmp = k // coin[i]
        cnt += tmp
        k -= coin[i] * tmp
print(cnt)