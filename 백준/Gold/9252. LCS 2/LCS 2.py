import sys
input = sys.stdin.readline

string1 = ['']+list(input().rstrip())
string2 = ['']+list(input().rstrip())
lcs = [['']*len(string2) for _ in range(len(string1))]

for i in range(1,len(string1)):
    for j in range(1,len(string2)):
        if string1[i] == string2[j]:
            lcs[i][j] = lcs[i-1][j-1] + string1[i]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

result = lcs[-1][-1]
print(len(result), result, sep="\n")