from collections import deque

n,k = map(int, input().split())
belt = list(map(int,input().split()))

b = deque(belt)
robot = deque([0]*n*2)

res = 0
cnt = 0
for i in range(n * 2):
    if b[i] == 0:
        cnt += 1

while True:
    res += 1
    # 과정 1
    if robot[n-1] > 0:
        robot[n-1] = 0
    bPop = b.pop()
    b.appendleft(bPop)
    robotPop = robot.pop()
    robot.appendleft(robotPop)
    # 과정 2
    for i in range(n-1,-1,-1):
        # 내려야할 위치면 로봇 내리기
        if i == n-1 and robot[i] > 0:
            robot[i] = 0
        # 다음칸의 내구성이 1이상이고 빈칸이면 로봇을 한칸 움직이기
        if b[i+1] > 0 and robot[i+1] == 0 and robot[i] > 0:
            robot[i] = 0
            robot[i+1] = 1
            b[i+1] -= 1
            if b[i+1] == 0:
                cnt += 1

    # 과정 3
    if b[0] > 0:
        robot[0] = 1
        b[0] -= 1
        if b[0] == 0:
            cnt += 1

    # 과정 4
    if cnt >= k:
        break

print(res)