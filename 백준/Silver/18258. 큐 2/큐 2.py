import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = []
q = deque()
for _ in range(n):
    tmp = input().split()
    oper = tmp[0]
    if len(tmp) > 1:
        k = int(tmp[1])

    if oper == 'push':
        q.append(k)
    elif oper == 'pop':
        if q:
            ans.append(q.popleft())
        else:
            ans.append(-1)
    elif oper == 'size':
        ans.append(len(q))
    elif oper == 'empty':
        if q:
            ans.append(0)
        else:
            ans.append(1)
    elif oper == 'front':
        if q:
            ans.append(q[0])
        else:
            ans.append(-1)
    else:
        if q:
            ans.append(q[-1])
        else:
            ans.append(-1)

print(*ans,sep='\n')