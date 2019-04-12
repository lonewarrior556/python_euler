triangles = open("p102_triangles.txt", "r").readlines()

countNoCheck1=0
countNoCheck2=0
countUnkown=0

def checkSide(x3, y3, x2, y2, x1, y1):
    val = ((x3 - x1) * (y2 - y1)) - ((y3 - y1) * (x2 - x1))
    if val < 0: return -1
    if val > 0: return 1
    raise Exception('should not happen')

for triangle in triangles:
    points = map(int, triangle.strip().split(','))
    x1, y1 = points[0:2]
    x2, y2 = points[2:4]
    x3, y3 = points[4:6]
    # if x1 < 0 and x2 < 0 and x3 < 0:
    #     countNoCheck1+=1
    #     continue
    # if x1 > 0 and x2 > 0 and x3 > 0:
    #     countNoCheck1+=1
    #     continue
    # if y1 < 0 and y2 < 0 and y3 < 0:
    #     countNoCheck1+=1
    #     continue
    # if y1 > 0 and y2 > 0 and y3 > 0:
    #     countNoCheck1+=1
    #     continue
    a1 = checkSide(x3, y3, x2, y2, x1, y1)
    a2 = checkSide(0, 0, x2, y2, x1, y1)

    b1 = checkSide(x2, y2, x3, y3, x1, y1)
    b2 = checkSide(0, 0, x3, y3, x1, y1)

    c1 = checkSide(x1, y1, x3, y3, x2, y2)
    c2 = checkSide(0, 0, x3, y3, x2, y2)

    if a1 != a2:
        countNoCheck2+=1
        continue

    if b1 != b2:
        countNoCheck2+=1
        continue

    if c1 != c2:
        countNoCheck2+=1
        continue

    # print  str(x1) + ',' + str(y1)
    # print  str(x2) + ',' + str(y2)
    # print  str(x3) + ',' + str(y3)

    countUnkown+=1

print 'countNoCheck1:', countNoCheck1
print 'countNoCheck2:', countNoCheck2
print 'countUnkown:', countUnkown
