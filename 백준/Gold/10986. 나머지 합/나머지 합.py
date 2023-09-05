import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
remainArr = [0]*m
sumV = 0
for i in range(n):
    sumV += arr[i]
    remainArr[sumV % m] += 1

res = remainArr[0]
for i in range(m):
    res += (remainArr[i] * (remainArr[i]-1))//2

print(res)