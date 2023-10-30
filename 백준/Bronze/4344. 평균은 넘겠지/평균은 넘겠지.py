import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    arr = list(map(int,input().split()))
    cnt = arr[0]
    sumV = sum(arr) - cnt
    average = sumV//cnt
    upCnt = 0
    for i in range(cnt):
        if arr[i+1] > average:
            upCnt += 1
    res = (upCnt/cnt)*100
    print(f"{res:.3f}%")
