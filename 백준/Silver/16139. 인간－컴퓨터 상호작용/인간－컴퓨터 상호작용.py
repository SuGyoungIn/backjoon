import sys
input = sys.stdin.readline

S = input().rstrip()
T = int(input())
ans = []
for _ in range(T):
    q = list(map(str,input().rstrip().split()))
    a = q[0]
    l = int(q[1])
    r = int(q[2])
    cnt = 0
    for i in range(l,r+1):
        if S[i] == a:
            cnt += 1

    ans.append(cnt)

print(*ans,sep='\n')
