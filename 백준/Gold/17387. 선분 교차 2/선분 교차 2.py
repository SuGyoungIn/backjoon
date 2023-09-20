x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
dot1 = (x1,y1)
dot2 = (x2,y2)
dot3 = (x3,y3)
dot4 = (x4,y4)

def ccw(dot1,dot2,dot3):
    x1,y1 = dot1
    x2,y2 = dot2
    x3,y3 = dot3

    s1 = (x1*y2)+(x2*y3)+(x3*y1)
    s2 = (y1*x2)+(y2*x3)+(y3*x1)

    if s1-s2 > 0:
        return 1
    elif s1-s2 == 0:
        return 0
    else:
        return -1

v1 = ccw(dot1,dot2,dot3)
v2 = ccw(dot1,dot2,dot4)
v3 = ccw(dot3,dot4,dot1)
v4 = ccw(dot3,dot4,dot2)

res = 0
flag = 0
if v1*v2 == 0 and v3*v4 == 0:
    flag = 1
    comX1 = (dot1[0],dot2[0])
    comX2 = (dot3[0],dot4[0])
    comY1 = (dot1[1],dot2[1])
    comY2 = (dot3[1],dot4[1])
    if min(comX1) <= max(comX2) and min(comX2) <= max(comX1) and min(comY1) <= max(comY2) and min(comY2) <= max(comY1):
        res = 1

if v1*v2 <= 0 and v3*v4 <= 0 and flag == 0:
    res = 1

print(res)