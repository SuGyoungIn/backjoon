def solution(n):
    answer = []
    arr = []
    for i in range(1,n+1):
        arr.append([0]*i)
    d = 1
    num = 1
    i = 0
    j = 0
    sumV = 0 
    for k in range(1,n+1):
        sumV += k
    while num <= sumV:
        if d%3 == 1:
            if 0<=i<n and arr[i][j] == 0:
                arr[i][j] = num
                num += 1
                i += 1
            else:
                d += 1
                j += 1
                i -= 1
        elif d%3 == 2:
            if 0<=j<len(arr[i]) and arr[i][j] == 0:
                arr[i][j] = num
                num += 1
                j += 1
            else:
                d += 1
                i -= 1
                j -= 2
        else:
            if 0<=i<n and arr[i][j] == 0:
                arr[i][j] = num
                num += 1
                i -= 1
                j -= 1
            else:
                d += 1
                i += 2
                j += 1
    for i in range(n):
        for j in range(len(arr[i])):
            answer.append(arr[i][j])
    return answer