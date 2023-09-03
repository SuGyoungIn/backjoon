n = int(input())
num = list(map(int,input().split()))

op = list(map(int,input().split()))
minV = 10**9
maxV = -(10**9)

def calc(res,nextIdx,plus,minus,multi,div):
    global minV
    global maxV

    if nextIdx == n:
        if res < minV:
            minV = res
        if res > maxV:
            maxV = res
        return

    if plus > 0:
        tmp = res
        tmp += num[nextIdx]
        calc(tmp,nextIdx+1,plus-1,minus,multi,div)
    if minus > 0:
        tmp = res
        tmp -= num[nextIdx]
        calc(tmp,nextIdx+1,plus,minus-1,multi,div)
    if multi > 0:
        tmp = res
        tmp *= num[nextIdx]
        calc(tmp,nextIdx+1,plus,minus,multi-1,div)
    if div > 0:
        tmp = res
        if tmp < 0:
            tmp *= -1
            tmp //= num[nextIdx]
            calc(-tmp, nextIdx + 1, plus, minus, multi, div - 1)
        else:
            tmp //= num[nextIdx]
            calc(tmp,nextIdx+1,plus,minus,multi,div-1)


calc(num[0],1,op[0],op[1],op[2],op[3])

print(maxV)
print(minV)