n = int(input())

f = n // 5
t = (n - (5 * f))//3

while f > 0:
    if (5 * f) + (3 * t) == n:
        break

    f -= 1
    tmp = n - (5 * f)
    t = tmp // 3

if (5 * f) + (3 * t) != n:
    print(-1)
else:
    print(f+t)