import sys
input = sys.stdin.readline
n = int(input())
line = [int(input()) for _ in range(n)]
stack = []
res = 0
for l in line:
    while stack and stack[-1][0] < l:
        res += stack.pop()[1]

    if not stack:
        stack.append((l,1))
    else:
        if stack[-1][0] == l:
            cnt = stack.pop()[1]
            res += cnt
            if stack:
                res += 1
            stack.append((l,cnt+1))
        else:
            stack.append((l,1))
            res += 1

print(res)