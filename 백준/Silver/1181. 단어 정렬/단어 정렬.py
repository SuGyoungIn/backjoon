import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(input().rstrip())

setArr = list(set(arr))
setArr.sort()
setArr.sort(key=lambda x:len(x))

print(*setArr,sep='\n')