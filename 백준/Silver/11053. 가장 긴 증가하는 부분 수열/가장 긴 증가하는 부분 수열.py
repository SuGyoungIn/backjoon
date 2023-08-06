import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

cnt = [1]*n
for i in range(1,n):
    tmp = 0
    for j in range(i,-1,-1):
        if arr[i] > arr[j] and cnt[j] > tmp:
            tmp = cnt[j]
    cnt[i] = tmp + 1

print(max(cnt))