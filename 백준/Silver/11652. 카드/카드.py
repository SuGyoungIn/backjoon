import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for _ in range(n):
    k = int(input())
    if k in dict:
        dict[k] += 1
    else:
        dict[k] = 1

arr = sorted(dict.items(), key = lambda x:(x[1],-x[0]))
print(arr[-1][0])