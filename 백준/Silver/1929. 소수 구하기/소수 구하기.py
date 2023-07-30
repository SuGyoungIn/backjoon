m,n = map(int,input().split())

arr = [1]*(n+1)
arr[0], arr[1] = 0, 0
for i in range(2,n+1):
    if arr[i] == 0:
        continue
    for j in range(2,n):
        if i*j > n:
            break
        arr[i*j] = 0

for i in range(m,n+1):
    if arr[i] > 0:
        print(i)