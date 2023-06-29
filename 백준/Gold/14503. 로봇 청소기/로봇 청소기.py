n,m = map(int,input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
clean = 0
dd = [[0,1],[0,-1],[1,0],[-1,0]]
rotateB = [[1,0],[0,-1],[-1,0],[0,1]] # 후진하기 위한 방향
rotateD = [[-1,0],[0,1],[1,0],[0,-1]] # 전진하기 위한 방향
while True:
    # 현재 칸 청소
    if room[r][c] == 0:
        clean += 1
        room[r][c] = -1

    # 현재 칸의 주변 4칸 확인
    isClean = 0
    for dx,dy in dd:
        ni,nj = r+dx, c+dy
        if 0<=ni<n and 0 <=nj<=m:
            if room[ni][nj] != 0:
                isClean += 1
            else:
                break

    if isClean == 4: # 주변에 청소되지 않은 빈칸이 없는 경우
        dx, dy = rotateB[d]
        if 0<=r+dx<n and 0<=c+dy<m and room[r+dx][c+dy] != 1:
            r += dx
            c += dy
        else:
            break
    else: # 주변에 청소되지 않은 빈칸이 있는 경우
        if d == 0:
            d = 3
        else:
            d -= 1
        dx,dy = rotateD[d]
        if 0<=r+dx<n and 0<=c+dy<m and room[r+dx][c+dy] == 0:
            r += dx
            c += dy

print(clean)