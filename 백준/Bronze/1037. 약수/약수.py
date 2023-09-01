import sys
input = sys.stdin.readline

cnt = int(input())
arrA = list(map(int,input().split()))

minV = 1_000_001
maxV = 1

for i in range(cnt):
    if arrA[i] < minV:
        minV = arrA[i]

    if arrA[i] > maxV:
        maxV = arrA[i]

print(minV*maxV)