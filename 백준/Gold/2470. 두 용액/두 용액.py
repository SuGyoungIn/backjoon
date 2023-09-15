import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
diff = 2_000_000_000
res = []
s = 0
e = n-1
while s < e:
    tmp = arr[s]+arr[e]
    if abs(tmp) < diff:
        diff = abs(tmp)
        res = [arr[s],arr[e]]

    if tmp > 0:
        e -= 1
    elif tmp < 0:
        s += 1
    else:
        break

print(*res)
