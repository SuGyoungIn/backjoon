import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
ans = 0
arr.sort()
t = n-1
b = 0
while b < t:
    tmp = arr[t]+arr[b]
    if tmp < x:
        b += 1
    elif tmp > x:
        t -= 1
    else:
        ans += 1
        b += 1

print(ans)