import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
res = list()
res.append(-1)
stack = list()
stack.append(A[-1])
for i in range(n-2,-1,-1):
    while stack:
        tmp = stack.pop()
        if tmp > A[i]:
            res.append(tmp)
            stack.append(tmp)
            stack.append(A[i])
            break
    else:
        res.append(-1)
        stack.append(A[i])

res.reverse()
print(*res)