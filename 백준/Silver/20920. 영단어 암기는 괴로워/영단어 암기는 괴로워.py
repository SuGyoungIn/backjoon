import sys
input = sys.stdin.readline

n,m = map(int,input().split())
word = {}
res = []
for _ in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue

    if w in word:
        word[w] += 1
    else:
        word[w] = 1
        res.append(w)

res.sort()
res.sort(key=lambda x:(-word[x],-len(x)))
print(*res,sep='\n')