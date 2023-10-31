import sys
import math
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break

    sqrtV = int(math.sqrt(n))
    arr = []
    for i in range(1,sqrtV+1):
        if n % i == 0:
            arr.append(i)
    arr2 = []
    for ar in arr:
        arr2.append(n//ar)
    res = list(set(arr + arr2))
    res.sort()
    res.pop()
    if n == sum(res):
        string = str(n) + " = "
        for i in range(len(res)):
            if i == len(res) - 1:
                string += str(res[i])
            else:
                string += str(res[i]) + " + "
        print(string)
    else:
        print(str(n) + " is NOT perfect.")
