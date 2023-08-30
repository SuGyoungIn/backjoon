import sys
input = sys.stdin.readline

while True:
    stack = []
    string = list(input())
    if string[0] == '.':
       break
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
        else:
            continue

    if stack:
        print('no')
    else:
        print('yes')
