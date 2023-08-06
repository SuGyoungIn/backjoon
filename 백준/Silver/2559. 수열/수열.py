import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))


sumV = sum(arr[:k])
res = sumV
for i in range(k,n):
    sumV -= arr[i-k]
    sumV += arr[i]
    if res < sumV:
        res = sumV

print(res)