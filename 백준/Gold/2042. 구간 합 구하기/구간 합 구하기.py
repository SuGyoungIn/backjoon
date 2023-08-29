import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
treeHeight = 0
length = n

while length:
    length //= 2
    treeHeight += 1

treeSize = pow(2,treeHeight+1)
nodeStart = (treeSize // 2) - 1

tree = [0] * (treeSize+1)

for i in range(nodeStart+1, nodeStart+1+n):
    tree[i] = int(input())

def init(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

init(treeSize-1)


def change(idx,val):
    diff = val - tree[idx]
    while idx:
        tree[idx] = tree[idx] + diff
        idx = idx // 2

def sumV(s,e):
    tmp = 0
    while s <= e:
        if s % 2:
            tmp += tree[s]
            s += 1
        if not e % 2:
            tmp += tree[e]
            e -= 1

        s //= 2
        e //= 2
    return tmp

res = []

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        change(nodeStart+b,c)
    else:
        b = b + nodeStart
        c = c + nodeStart
        res.append(sumV(b,c))

print(*res, sep='\n')