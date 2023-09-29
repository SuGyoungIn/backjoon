import sys
input = sys.stdin.readline

n,m = map(int,input().split())
noHeard = set()
noSee = set()

for _ in range(n):
    noHeard.add(input().rstrip())

for _ in range(m):
    noSee.add(input().rstrip())

noHeardSee = list(noHeard & noSee)
print(len(noHeardSee))
noHeardSee.sort()
print(*noHeardSee,sep='\n')