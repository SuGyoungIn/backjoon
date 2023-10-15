n = int(input())
beads = list(map(int,input().split()))
res = []
m = int(input())
case = list(map(int,input().split()))

dp = [[0]*15001 for _ in range(n+1)]

def cal(num,w):
    if num > n:
        return
    if dp[num][w]:
        return

    dp[num][w] = 1
    cal(num+1,w)
    cal(num+1,w+beads[num-1])
    cal(num+1,abs(w-beads[num-1]))

cal(0,0)

for c in case:
    if c > 15000:
        res.append('N')
        continue
    if dp[n][c] == 1:
        res.append('Y')
    else:
        res.append('N')

print(*res)