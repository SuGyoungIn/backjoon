import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
res = [-1]*n
stack = list()
stack.append(A[-1])
for i in range(n-2,-1,-1):
    while stack:
        tmp = stack.pop()
        if tmp > A[i]:
            res[i] = tmp
            stack.append(tmp)
            stack.append(A[i])
            break
    else:
        stack.append(A[i])

print(*res)