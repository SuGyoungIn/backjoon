def factor(num):
    if num == 1:
        return 1
    else:
        return num * factor(num-1)

n,k = map(int,input().split())
if k == 0 or n == k:
    print(1)
elif k == 1:
    print(n)
else:
    print(factor(n)//(factor(k)*factor(n-k)))