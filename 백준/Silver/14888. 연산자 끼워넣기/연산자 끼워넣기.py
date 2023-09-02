from itertools import permutations
from collections import deque


def f(op, arr):
    q = deque(arr)

    for o in op:
        a = q.popleft()
        b = q.popleft()

        if o == '+':
            q.appendleft(a+b)
        elif o == '-':
            q.appendleft(a-b)
        elif o == '*':
            q.appendleft(a*b)
        else:
            if a < 0 and b > 0:
                q.appendleft(-(-a//b))
            else:
                q.appendleft(a // b)
    return q[0]


n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

oper =(['+']*operator[0]) + (['-']*operator[1]) + (['*']*operator[2]) + (['/']*operator[3])

maxV = -(10**9)
minV = 10**9

for op in permutations(oper,n-1):
    res = f(op, arr)
    if res > maxV:
        maxV = res

    if res < minV:
        minV = res

print(maxV)
print(minV)