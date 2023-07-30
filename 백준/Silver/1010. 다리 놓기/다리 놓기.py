T = int(input())

for t in range(T):
    n,m = map(int,input().split())
    if n == 1:
        print(m)
    elif 1 < n < m:
        res = 1
        for i in range(m,m-n,-1):
            res *= i
        div = 1
        for i in range(n,0,-1):
            div *= i
        print(res//div)
    else:
        print(1)