import sys
from collections import deque
input = sys.stdin.readline

s,e = map(int,input().split())
q = deque()
v = [-1]*100001
v[s] = 0
q.append((0,s))
d = [2,1,-1]
while q:
    sec,now = q.popleft()
    if now == e:
        break
    else:
        for di in d:
            if di == 2:
                next = now*2
                if 0<=next<100001 and v[next] == -1:
                    v[next] = sec+1
                    q.append((sec+1,next))
            else:
                next = now+di
                if 0<=next<100001 and v[next] == -1:
                    v[next] = sec+1
                    q.append((sec+1,next))

print(v[e])
sec = v[e]
loc = e
path = [0]*(sec+1)
path[sec] = loc
idx = sec-1
while sec > 0:
    if 0<=loc-1<100001 and v[loc-1] == sec-1:
        path[idx] = loc-1
        loc -= 1
    elif 0<=loc+1<100001 and v[loc+1] == sec-1:
        path[idx] = loc+1
        loc += 1
    elif 0<=loc//2<100001 and v[loc//2] == sec-1:
        path[idx] = loc//2
        loc //= 2

    sec -= 1
    idx -= 1

print(*path)