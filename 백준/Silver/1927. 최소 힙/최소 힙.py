import sys
input = sys.stdin.readline
arr = []
n = int(input())
def minHeapPush(x):
    arr.append(x)
    current = len(arr) - 1
    while current > 0:
        parent = (current-1) // 2
        if arr[parent] > arr[current]:
            arr[parent], arr[current] = arr[current], arr[parent]
            current = parent
        else:
            break

def minHeapPop():
    popV,arr[0] = arr[0],arr.pop()
    current,child = 0,1
    while child < len(arr):
        sibling = child + 1
        if sibling < len(arr) and arr[child] > arr[sibling]:
            child = sibling
        if arr[current] > arr[child]:
            arr[current],arr[child] = arr[child],arr[current]
            current = child
            child = (current * 2) + 1
        else:
            break
    return popV


res = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr:
            if len(arr) == 1:
                res.append(arr.pop())
            else:
                res.append(minHeapPop())
        else:
            res.append(0)
    else:
        minHeapPush(x)

print(*res, sep='\n')