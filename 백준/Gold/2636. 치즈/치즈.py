import sys

input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

hour = 0
cnt = 0

def checkChease(arr):
    tmpCnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                tmpCnt += 1

    return tmpCnt


while True:
    cheaseCnt = checkChease(board)
    if cheaseCnt == 0:
        break
    else:
        cnt = cheaseCnt
        hour += 1
        stack = list()
        stack.append((0,0))
        visited = list([0]*m for _ in range(n))
        while len(stack) > 0:
            i,j = stack.pop()
            visited[i][j] = 1
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = i+dx, j+dy
                if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0:
                    if board[ni][nj] == 0:
                        stack.append((ni,nj))
                    else:
                        board[ni][nj] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0

print(hour)
print(cnt)