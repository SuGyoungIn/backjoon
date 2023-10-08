import sys
input = sys.stdin.readline

S = input().rstrip()
T = int(input())

n = len(S)
alpha = [[0]*n for _ in range(26)]

alpha[ord(S[0])-97][0] += 1

for j in range(1,n):
    for i in range(26):
        if ord(S[j]) - 97 == i:
            alpha[i][j] = alpha[i][j-1] + 1
        else:
            alpha[i][j] = alpha[i][j-1]

ans = []
for _ in range(T):
    q = list(map(str,input().rstrip().split()))
    a,l,r = q[0],int(q[1]),int(q[2])
    idx = ord(a)-97

    if l == 0:
        ans.append(alpha[idx][r])
    else:
        ans.append(alpha[idx][r] - alpha[idx][l-1])

print(*ans,sep='\n')