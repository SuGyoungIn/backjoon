import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

res = 100001
start = 0
end = 0
tmp = arr[0]
while start<n:
    if tmp < s:
        if end < n-1:
            end += 1
            tmp += arr[end]
        else:
            break
    else:
        if res > end-start+1:
            res = end-start+1
        tmp -= arr[start]
        start += 1

if res > n:
    print(0)
else:
    print(res)