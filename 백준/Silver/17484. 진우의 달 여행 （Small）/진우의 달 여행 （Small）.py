n,m = map(int,input().split())
path = [list(map(int, input().split())) for _ in range(n)]

oil = list([[] for _ in range(m)] for _ in range(n))

for j in range(m):
    oil[0][j] = [path[0][j],path[0][j],path[0][j]]


for i in range(1,n):
    for j in range(m):
        oil[i][j] = [path[i][j],path[i][j],path[i][j]]
        if 0<=j-1<m:
            oil[i][j][0] += min(oil[i - 1][j - 1][1], oil[i-1][j - 1][2])
        else:
            oil[i][j][0] = 1000

        oil[i][j][1] += min(oil[i - 1][j][0], oil[i - 1][j][2])

        if 0<=j+1<m:
            oil[i][j][2] += min(oil[i - 1][j+1][0], oil[i - 1][j+1][1])
        else:
            oil[i][j][2] = 1000


answer = 1000000

for j in range(m):
    minV = min(oil[n-1][j])
    if answer > minV:
        answer = minV

print(answer)