import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

maxV = 0
stack = []
for i in range(n):
    height = arr[i]
    while stack and stack[-1][1] > height:
        s_idx, s_height = stack.pop()
        width = i
        if stack:
            width = i - stack[-1][0] -1
        v = width*s_height
        maxV = max(maxV,v)

    stack.append((i,height))

while stack:
    s_idx, s_height = stack.pop()
    width = n
    if stack:
        width = n - stack[-1][0]-1
    v = width*s_height
    maxV = max(maxV, v)

print(maxV)