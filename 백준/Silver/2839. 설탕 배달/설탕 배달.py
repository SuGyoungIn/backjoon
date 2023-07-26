n = int(input())

res = 5000
candiFive = n // 5
candiThree = (n - (5 * candiFive))//3

while candiFive > 0:
    if (5 * candiFive) + (3 * candiThree) == n:
        break

    candiFive -= 1
    tmp = n - (5 * candiFive)
    candiThree = tmp // 3

if (5 * candiFive) + (3 * candiThree) != n:
    print(-1)
else:
    print(candiFive+candiThree)
