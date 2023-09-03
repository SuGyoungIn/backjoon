import sys
sys.setrecursionlimit(10**6)
n = int(input())


def hanoi(cnt,start,goal,other):
    if cnt == 1:
        print(start,goal)
        return
    if cnt == 0:
        return
    hanoi(cnt-1,start,other,goal)
    hanoi(1,start,goal,other)
    hanoi(cnt-1,other,goal,start)

print(2**n - 1)
hanoi(n,1,3,2)