def findTime(arr,t):
    sumP = 0
    for a in arr:
        sumP += t // a
    return sumP

def solution(n, times):
    judge = sorted(times)
    minT = 1
    maxT = n*max(judge)
    
    while minT <= maxT:
        midT = (minT + maxT) // 2
        if findTime(judge, midT) >= n:
            maxT = midT - 1
        else:
            minT = midT + 1
    
    
    return minT