import sys
input = sys.stdin.readline

def union(a,b,parents,cnt):
    find_a = find(a,parents)
    find_b = find(b,parents)
    if find_a != find_b:
        cnt[find_a] += cnt[find_b]
    parents[find_b] = find_a
    return

def find(a,parents):
    if a == parents[a]:
        return a
    else:
        parents[a] = find(parents[a],parents)
    return parents[a]


T = int(input())
res = []
for t in range(T):
    F = int(input())
    parents = {}
    cnt = {}
    for f in range(F):
        a,b = map(str, input().split())
        if a not in parents:
            parents[a] = a
            cnt[a] = 1
        if b not in parents:
            parents[b] = b
            cnt[b] = 1
        union(a,b,parents,cnt)
        res.append(cnt[parents[a]])

print(*res, sep='\n')