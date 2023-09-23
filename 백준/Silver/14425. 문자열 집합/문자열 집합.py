import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

s = [sys.stdin.readline().rstrip() for _ in range(n)]
list_m = [sys.stdin.readline().rstrip() for _ in range(m)]

cnt = 0
set_s = set(s)
for val in list_m:
    list_m = val.split(' ')
    set_m = set(list_m)
    if len(set_s & set_m):
        cnt += 1

print(cnt)