import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
res = [-1]*n
stack = []
for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] > A[i]:
            res[i] = stack[-1]
            break
        else:
            stack.pop()

    stack.append(A[i])

print(*res)