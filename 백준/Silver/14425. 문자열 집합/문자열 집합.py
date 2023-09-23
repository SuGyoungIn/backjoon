import sys
input = sys.stdin.readline
n,m = map(int,input().split())
res = 0
S = set()
for _ in range(n):
    S.add(input())

for _ in range(m):
    tmp = []
    tmp.append(input())
    tmp = set(tmp)
    if S & tmp:
        res += 1
print(res)