from collections import deque
n,m = map(int,input().split())
ladderS = []
ladderE = []
snakeS = []
snakeE = []
for _ in range(n):
    s,e = map(int,input().split())
    ladderS.append(s-1)
    ladderE.append(e-1)
for _ in range(m):
    s,e = map(int,input().split())
    snakeS.append(s-1)
    snakeE.append(e-1)

q = deque()
q.append((0,0))
v = [0]*100
v[0] = 1
while q:
    cnt,p = q.popleft()
    if p == 99:
        v[99] = min(v[99],cnt)
    for i in range(1,7):
        flag = 0
        if p+i <= 99 and v[p+i] == 0:
            v[p+i] = cnt+1
            for j in range(n):
                if p+i == ladderS[j]:
                    v[ladderE[j]] = cnt+1
                    flag = 1
                    q.append((cnt+1,ladderE[j]))
            if flag == 0:
                for j in range(m):
                    if p+i == snakeS[j]:
                        v[snakeE[j]] = cnt+1
                        flag = 1
                        q.append((cnt+1,snakeE[j]))

            if flag == 0:
                q.append((cnt+1,p+i))

print(v[99])