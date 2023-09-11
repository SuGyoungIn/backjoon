import sys
input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()
stack = []
n = len(boom)
for s in string:
    if s == boom[-1]:
        stack.append(s)
        if len(stack) >= n:
            start = len(stack) - n
            cnt = 0
            for i in range(n):
                if stack[start+i] == boom[i]:
                    cnt += 1
            if cnt == n:
                for _ in range(n):
                    stack.pop()
    else:
        stack.append(s)

if stack:
    print(''.join(stack))
else:
    print("FRULA")