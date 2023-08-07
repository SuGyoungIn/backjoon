from collections import deque
n,m = map(int,input().split())
ladder = []
snake = []

for _ in range(n):
    s,e = map(int,input().split())
    ladder.append((s-1,e-1))

for _ in range(m):
    s,e = map(int,input().split())
    snake.append((s-1,e-1))

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
            for ls,le in ladder:
                if p+i == ls:
                    v[le] = cnt+1
                    flag = 1
                    q.append((cnt+1,le))
            if flag == 0:
                for ss,se in snake:
                    if p+i == ss:
                        v[se] = cnt+1
                        flag = 1
                        q.append((cnt+1,se))

            if flag == 0:
                q.append((cnt+1,p+i))

print(v[99])