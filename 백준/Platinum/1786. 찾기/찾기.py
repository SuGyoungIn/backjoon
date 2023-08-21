import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

n = len(T)
m = len(P)
check = [0]*m
j = 0
for i in range(1,m):
    while j > 0 and P[i] != P[j]:
        j = check[j-1]
    if P[i] == P[j]:
        j += 1
        check[i] += j

k = 0
res=[]
for i in range(n):
    while k > 0 and T[i] != P[k]:
        k = check[k-1]
    if T[i] == P[k]:
        if k == m - 1:
            res.append(i-m+2)
            k = check[k]
        else:
            k += 1

print(len(res))
print(*res)