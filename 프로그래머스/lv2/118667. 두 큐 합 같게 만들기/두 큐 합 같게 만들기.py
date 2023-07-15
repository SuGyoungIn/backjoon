from collections import deque

def solution(queue1, queue2):
    answer = -2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = (sum1+sum2) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    cntq = len(q1) + len(q2)
    candisum1 = []
    candisum2 = []
    cnt = 0
    flag = 0
    while True:
        if len(q1) == 0 or len(q2) == 0:
            flag = 1
            break
        if sum1 > sum2:
            cnt += 1
            tmp = q1.popleft()
            sum1 -= tmp
            q2.append(tmp)
            sum2 += tmp
        elif sum1 < sum2:
            cnt += 1
            tmp = q2.popleft()
            sum2 -= tmp
            q1.append(tmp)
            sum1 += tmp
        else:
            break
            
        if cnt > cntq+100:
            flag = 1
            break
    
    if flag == 0:
        answer = cnt
    else:
        answer = -1
            
    return answer