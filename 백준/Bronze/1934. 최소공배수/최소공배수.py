import sys
input = sys.stdin.readline

prime = [0]*45001
prime[0], prime[1] = -1, -1
for i in range(2,45001):
    if prime[i] == 0:
        prime[i] = 1
        for j in range(2,45001):
            if i*j > 45000:
                break
            else:
                prime[i*j] = -1
primeNumber = []
for i in range(45001):
    if prime[i] == 1:
        primeNumber.append(i)

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    multi = []
    if a == b:
        print(a)
        continue
    elif a > b:
        if a%b == 0:
            print(a)
            continue
    elif a < b:
        if b%a == 0:
            print(b)
            continue

    if prime[a] == 1 and prime[b] == 1:
        print(a*b)
        continue

    for num in primeNumber:
        tmp = num
        if num > a and num > b:
            break

        if a%num == 0 and b%num == 0:
            for i in range(2,16):
                pn = pow(num,i)
                if pn > a and pn > b:
                    break
                if a >= pn and a%pn == 0:
                    tmp = max(tmp,pn)
                if b >= pn and b%pn == 0:
                    tmp = max(tmp,pn)
            multi.append(tmp)
        elif a%num == 0:
            for i in range(2,16):
                pn = pow(num,i)
                if pn > a:
                    break
                if a >= pn and a%pn == 0:
                    tmp = max(tmp,pn)
            multi.append(tmp)
        elif b%num == 0:
            for i in range(2,16):
                pn = pow(num,i)
                if pn > b:
                    break
                if b >= pn and b%pn == 0:
                    tmp = max(tmp,pn)
            multi.append(tmp)

    res = 1
    for m in multi:
        res *= m

    print(res)