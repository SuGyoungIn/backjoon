import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
res = [0]*n
stack = []
for i in range(n-1,-1,-1):
    if not stack:
        stack.append((tops[i],i))
    else:
        while stack:
            if stack[-1][0] <= tops[i]:
                idx = stack[-1][1]
                res[idx] = i+1
                stack.pop()
            else:
                break
        stack.append((tops[i], i))

print(*res)