def getTree(h):
    sumV = 0
    for t in trees:
        if t > h:
            sumV += t-h
    return sumV


n,m = map(int, input().split())
trees = list(map(int,input().split()))
minM = 0
maxM = 2000000000

while minM <= maxM:
    midM = (minM + maxM)//2
    if getTree(midM) >= m:
        minM = midM + 1
    else:
        maxM = midM - 1

print(maxM)