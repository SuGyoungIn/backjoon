x = int(input())
n = int(input())
res = 0
for _ in range(n):
    a,b = map(int,input().split())
    res += a*b

if res == x:
    print('Yes')
else:
    print('No')