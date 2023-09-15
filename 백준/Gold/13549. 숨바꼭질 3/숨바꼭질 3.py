from collections import deque

s,e = map(int,input().split())
v = [-1]*150001
q = deque()
v[s] = 0
q.append((0,s))

d = [2,1,-1]
while q:
    sec,pos = q.popleft()
    if pos == e:
        break
    for di in d:
        if di == 2:
            j = pos*2
            while 0 < j < 150001:
                if v[j] == -1:
                    v[j] = sec
                    q.append((sec, j))
                else:
                    v[j] = min(v[j],sec)

                j *= 2
        else:
            if 0<= pos+di <150001 and v[pos+di]==-1:
                v[pos+di]=sec+1
                q.append((sec+1,pos+di))

print(v[e])