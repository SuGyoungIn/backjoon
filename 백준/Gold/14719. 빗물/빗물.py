def cntDrop(idx,arr,hIdx):
    stack = []
    cnt = 0
    start = arr[idx]
    if idx == 0:
        while idx <= hIdx:
            if arr[idx] >= start:
                while stack:
                    tmp = stack.pop()
                    cnt += start - tmp
                start = arr[idx]
            else:
                stack.append(arr[idx])

            idx += 1
    else:
        while idx >= hIdx:
            if arr[idx] >= start:
                while stack:
                    tmp = stack.pop()
                    cnt += start - tmp
                start = arr[idx]
            else:
                stack.append(arr[idx])

            idx -= 1

    return cnt


h,w = map(int, input().split())
land = list(map(int,input().split()))
res = 0

highIdx = land.index(max(land))
if highIdx == 0 or highIdx == 1:
    # 오른쪽에서부터 빗물 세기
    res += cntDrop(w-1,land,highIdx)
elif 1 < highIdx < w-3:
    # 왼쪽에서부터 빗물세기
    res += cntDrop(0,land,highIdx)
    # 오른쪽에서부터 빗물세기
    res += cntDrop(w-1,land,highIdx)
else:
    # 왼쪽에서부터 빗물세기
    res += cntDrop(0,land,highIdx)

print(res)