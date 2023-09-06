import sys
input = sys.stdin.readline

n = int(input())
table = []
for i in range(n):
    s,e = map(int,input().split())
    table.append([s,e])

table = sorted(table, key=lambda x:(x[1],x[0]))

end = 0
res = 0
for i in range(n):
    s,e = table[i]
    if s >= end:
        end = e
        res += 1

print(res)