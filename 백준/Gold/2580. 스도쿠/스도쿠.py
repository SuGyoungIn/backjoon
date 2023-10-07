import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(9)]
blank = []

def checkRow(i,num):
    for k in range(9):
        if num == board[i][k]:
            return False
    return True

def checkCol(j,num):
    for k in range(9):
        if num == board[k][j]:
            return False
    return True

def checkThree(i,j,num):
    ni = (i//3)*3
    nj = (j//3)*3
    for x in range(3):
        for y in range(3):
            if num == board[ni+x][nj+y]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit()

    for num in range(1,10):
        ni = blank[idx][0]
        nj = blank[idx][1]

        if checkRow(ni,num) and checkCol(nj,num) and checkThree(ni,nj,num):
            board[ni][nj] = num
            dfs(idx+1)
            board[ni][nj] = 0


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

dfs(0)