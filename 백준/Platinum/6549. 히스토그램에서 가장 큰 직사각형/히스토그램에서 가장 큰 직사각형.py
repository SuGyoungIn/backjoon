import sys
input = sys.stdin.readline

ans = []
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    maxV = 0
    stack = []
    for i in range(1,n+1):
        idx = i
        height = arr[i]
        while stack and stack[-1][1] > height:
            s_idx, s_height = stack.pop()
            width = i - 1
            if stack:
                width = i - stack[-1][0] - 1
            v = width*s_height
            maxV = max(maxV,v)

        stack.append((idx,height))

    while stack:
        s_idx, s_height = stack.pop()
        width = n
        if stack:
            width = n - stack[-1][0]
        v = width*s_height
        maxV = max(maxV, v)

    ans.append(maxV)
print(*ans, sep='\n')