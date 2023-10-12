import sys
input = sys.stdin.readline
n,c = map(int,input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

minV = 1
maxV = house[-1] - house[0]
res = 500000000

if c == 2:
    print(house[-1] - house[0])
else:
    while minV < maxV:
        mid = (minV + maxV) // 2
        cnt = 1
        tmp = house[0]
        for i in range(n):
            if house[i] - tmp >= mid:
                cnt += 1
                tmp = house[i]

        if cnt >= c:
            res = mid
            minV = mid+1
        elif cnt < c:
            maxV = mid

    print(res)