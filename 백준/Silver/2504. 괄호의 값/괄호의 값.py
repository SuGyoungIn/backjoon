string = input()

n = len(string)
if string[0] == ")" or string[0] == "]":
    print(0)
else:
    stack = []
    flag = 0
    for i in range(n):
        if string[i] == '(':
            if i+1 < n and string[i+1] == ")":
                stack.append(2)
            elif i+1 < n and not string[i+1] == ")":
                stack.append(string[i])
            else:
                flag = 1
                break
        elif string[i] == '[':
            if i+1 < n and string[i+1] == "]":
                stack.append(3)
            elif i+1 < n and not string[i+1] == "]":
                stack.append(string[i])
            else:
                break
        elif string[i] == ")":
            if len(stack) == 0:
                flag = 1
                break
            if 0<=i-1<n and string[i-1] == "(":
                continue
            sumV = 0
            check = 0
            while len(stack) > 0:
                last = stack.pop()
                if last == '(':
                    check = 1
                    break
                elif last == '[' or last == ']':
                    flag = 1
                    break
                else:
                    sumV += last
            if flag == 1:
                break
            else:
                if check == 1:
                    stack.append(sumV*2)
                else:
                    flag = 1
                    break
        else:
            if len(stack) == 0:
                flag = 1
                break
            if 0<=i-1<n and string[i-1] == "[":
                continue
            sumV = 0
            check = 0
            while len(stack) > 0:
                last = stack.pop()
                if last == '[':
                    check = 1
                    break
                elif last == '(' or last == ')':
                    flag = 1
                    break
                else:
                    sumV += last
            if flag == 1:
                break
            else:
                if check == 1:
                    stack.append(sumV * 3)
                else:
                    flag = 1
                    break

    if flag == 1:
        print(0)
    elif '(' in stack or ")" in stack or '[' in stack or ']' in stack:
        print(0)
    else:
        print(sum(stack))