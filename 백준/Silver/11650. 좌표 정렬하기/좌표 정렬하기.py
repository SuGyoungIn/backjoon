import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x:(x[0],x[1]))
for a,b in arr:
    print(a,b)