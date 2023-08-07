import math
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def doubleStr(strArr,dic):
    global union
    for i in range(1,len(strArr)):
        front = strArr[i-1].lower()
        now = strArr[i].lower()
        if front in alpha and now in alpha:
            tmp = front+now
            union += 1
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
            
def solution(str1, str2):
    global union
    dict1 = {}
    dict2 = {}
    union = 0 
    doubleStr(list(str1),dict1)
    doubleStr(list(str2),dict2)
    inter = 0

    for d in dict1:
        if d in dict2:
            inter += min(dict1[d],dict2[d])
             
    union -= inter
    if inter == 0 and union == 0:
        return 65536
    else:
        return math.floor((inter/union)*65536)
