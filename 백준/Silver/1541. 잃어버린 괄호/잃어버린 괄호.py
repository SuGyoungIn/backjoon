e = list(input())
exp = []

tmp = ''
for i in range(len(e)):
    if e[i] == '-' or e[i] == '+':
        exp.append(int(tmp))
        exp.append(e[i])
        tmp = ''
    else:
        tmp += e[i]
exp.append(int(tmp))

res = 0
minus = 0
oper = 1
for i in range(len(exp)):
    if i%2 == 0:
        if oper:
            res += exp[i]
        else:
            minus += exp[i]
    else:
        if not oper and exp[i] == '-':
            res -= minus
            minus = 0
        elif oper and exp[i] == '-':
            oper = 0

res -= minus
print(res)