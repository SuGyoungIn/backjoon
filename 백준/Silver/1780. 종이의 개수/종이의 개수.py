import sys
input = sys.stdin.readline

def cnt_paper(i,j,l):
    if l == 1:
        res[paper[i][j]+1] += 1
        return

    tmp = paper[i][j]
    flag = 0
    for ni in range(i,i+l):
        for nj in range(j,j+l):
            if paper[ni][nj] != tmp:
                flag = 1
                break
        if flag:
            break

    if not flag:
        res[tmp+1] += 1
    else:
        m = l//3
        for mi in range(3):
            for mj in range(3):
                cnt_paper(i+(mi*m),j+(mj*m),m)

    return

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
res = [0,0,0]
cnt_paper(0,0,n)
print(*res,sep='\n')
