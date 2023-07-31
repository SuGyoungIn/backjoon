import sys
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]
arr = [0]*8001

avgV = round(sum(number)/n)
for num in number:
    arr[num+4000] += 1

cenV = 0
flagC = 0
freqV = -5000
flagF = 0
maxFreV = max(arr)
minV = 5000
maxV = -5000
for i in range(8001):
    # 중앙값 찾기
    if arr[i] > 0:
        if cenV < (n//2)+1 and flagC == 0:
            cenV += arr[i]
            if cenV >= (n//2)+1:
                cenV = i - 4000
                flagC = 1
        # 최빈값 찾기, 여러개일 경우 두번째 값으로 갱신
        if arr[i] == maxFreV and flagF <= 1:
            freqV = i - 4000
            flagF += 1
        # 범위 찾기
        if minV > i - 4000:
            minV = i - 4000

        if maxV < i - 4000:
            maxV = i - 4000

print(avgV)
print(cenV)
print(freqV)
print(maxV-minV)