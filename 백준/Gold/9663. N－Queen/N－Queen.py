n = int(input())

def dfs(idx,board):
    if idx == n-1:
        return 1

    ans = 0
    for di in range(n):
        if di in board:
            continue
        for c in range(1,idx+2):
            if board[idx+1-c] == di - c or board[idx+1-c] == di + c:
                break
        else:
            board[idx+1] = di
            ans += dfs(idx+1,board)
            board[idx+1] = -1

    return ans


res = 0
for i in range(n):
    board = [-1] * n
    board[0] = i
    res += dfs(0,board)
print(res)