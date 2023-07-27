import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
cardCnt = {}
for c in card:
    if c in cardCnt:
        cardCnt[c] += 1
    else:
        cardCnt[c] = 1

m = int(input())
num = list(map(int,input().split()))
res = []
for n in num:
    if n in cardCnt:
        res.append(cardCnt[n])
    else:
        res.append(0)

print(*res)