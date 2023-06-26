n,d = map(int, input().split())
short = [list(map(int, input().split())) for _ in range(n)]

short.sort(key=lambda x:x[0])
path = []
for sh in short:
    s,e,l = sh[0],sh[1],sh[2]
    if e-s <= l or e > d:
        continue
    else:
        path.append(sh)

dp = [0]*(d+1)
for i in range(1,d+1):
    sc = 10000
    for p in path:
        s,e,l = p[0],p[1],p[2]
        if i == e:
            if sc > dp[s] + l:
                sc = dp[s] + l
    dp[i] = min(dp[i-1]+1, sc)

print(dp[d])