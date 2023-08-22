n,m = map(int,input().split())
res = []

def seq(string,next):
    if len(string) == m:
        res.append(list(string))
        return
    else:
        for i in range(next,n+1):
            string += str(i)
            seq(string,i)
            l = len(string) - 1
            string = string[:l]

tmp = ''
seq(tmp,1)

for r in res:
    print(*r)