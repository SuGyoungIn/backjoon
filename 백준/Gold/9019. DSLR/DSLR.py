import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    A,B = map(int,input().split())
    q = deque()
    res = ''
    q.append((A,res))
    v = [0]*10001
    v[A] = 1
    while q:
        num, txt = q.popleft()
        if num == B:
            res = txt
            break

        dNum = (num * 2) % 10000
        if v[dNum] == 0:
            v[dNum] = 1
            q.append((dNum,txt+'D'))

        sNum = num - 1 if num > 0 else 9999
        if v[sNum] == 0:
            v[sNum] = 1
            q.append((sNum,txt+'S'))

        strNum = str(num)
        if len(strNum) < 4:
            strNum = '0' * (4 - len(strNum)) + strNum
        lNum = int(strNum[1:] + strNum[0])

        if v[lNum] == 0:
            v[lNum] = 1
            q.append((lNum,txt+'L'))

        rNum = int(strNum[3]+strNum[:3])

        if v[rNum] == 0:
            v[rNum] = 1
            q.append((rNum,txt+'R'))

    ans.append(res)
print(*ans, sep='\n')