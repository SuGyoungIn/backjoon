import sys
input=sys.stdin.readline
m = int(input())
S = 0
for _ in range(m):
    operate = input().split()
    if operate[0] == 'all':
        S = (1 << 21) - 1
        continue
    elif operate[0] == 'empty':
        S = 0
        continue

    op = operate[0]
    x = int(operate[1])
    if op == 'add':
        S |= (1 << x)
    elif op == 'remove':
        S &= ~(1 << x)
    elif op == 'toggle':
        S ^= (1 << x)
    else:
        if S & (1 << x):
            print(1)
        else:
            print(0)