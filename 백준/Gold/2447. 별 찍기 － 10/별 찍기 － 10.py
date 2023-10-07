import sys
sys.setrecursionlimit(10**6)
n = int(input())

def make_star(k):
    if k == 1:
        return ['*']

    stars = make_star(k//3)
    star = []
    for s in stars:
        star.append(s*3)
    for s in stars:
        star.append(s+' '*(k//3)+s)
    for s in stars:
        star.append(s*3)

    return star

print('\n'.join(make_star(n)))