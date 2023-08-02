import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcP = input().rstrip()
    n = int(input())
    string = input().rstrip()
    arr = list(string[1:-1].split(','))
    cntR = 0
    flag = 0
    for p in funcP:
        if p == 'D':
            if n > 0:
                if cntR > 0 and cntR % 2:
                    arr.pop()
                else:
                    arr.pop(0)
                n -= 1
            else:
                flag = 1
                break
        else:
            cntR += 1
    if flag > 0:
        print('error')
    else:
        if cntR % 2:
            arr.reverse()
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr)+']')