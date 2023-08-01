import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ps = list(input().rstrip())
    stack = []
    if len(ps) % 2 == 1:
        print('NO')
    else:
        for p in ps:
            if p == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(p)
        if stack:
            print('NO')
        else:
            print('YES')