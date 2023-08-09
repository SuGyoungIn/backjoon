import sys
input = sys.stdin.readline
n = int(input())
number = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))
dicNum = {}
for num in number:
    if num not in dicNum:
        dicNum[num] = 1

for c in check:
    if c in dicNum:
        print(1)
    else:
        print(0)