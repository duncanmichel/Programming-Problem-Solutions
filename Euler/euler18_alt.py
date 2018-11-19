triangle = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def evalChild(lvl,row):
    child = triangle[lvl][row]
    if lvl == len(triangle) - 1:
        return child
    return child + max(evalChild(lvl+1,row),evalChild(lvl+1,row+1))
    
#broken, doesn't work
def poorChild(lvl,row):
    child = triangle[lvl][row]
    if lvl == len(triangle) - 1:
        return child
    elif triangle[lvl+1][row] > triangle[lvl+1][row+1]:
        return child + poorChild(lvl+1,row)
    else:
        return child + poorChild(lvl+1,row+1)

#broken, doesn't work
def bestDescendant(lvl,row):
    if lvl == len(triangle) - 1:
        return evalParent(lvl,row)
    elif triangle[lvl+1][row] > triangle[lvl+1][row+1]:
        return bestDescendant(lvl+1,row)
    else:
        return bestDescendant(lvl+1,row+1)

#broken, doesn't work
def evalParent(lvl,row):
    #print("[test] Current level: %s" % triangle[lvl])
    if row >= len(triangle[lvl]) or row<0:
        return 0
    elif lvl == 0:
        return triangle[lvl][row]
    else:
        x = max(evalParent(lvl-1,row),evalParent(lvl-1,row-1))
        #print("[test] Current child: %s" % x)
        return triangle[lvl][row] + x

def bestParent(lvl,row):
    parent = triangle[lvl][row]
    if lvl == 0:
        return parent
    elif row-1 < 0:
        return parent + bestParent(lvl-1,row)
    elif row >= len(triangle[lvl-1]):
        return parent + bestParent(lvl-1,row-1)
    elif triangle[lvl-1][row] > triangle[lvl-1][row-1]:
        return parent + bestParent(lvl-1,row)
    elif triangle[lvl-1][row] > triangle[lvl-1][row-1]:
        return parent + bestParent(lvl-1,row-1)
    else:
        return parent + max(bestParent(lvl-1,row-1),bestParent(lvl-1,row))

    
def newTree(lvl,row):
    return 0

def brute():
    return triangle[0][0] + max(evalChild(1,0),evalChild(1,1)) 
    
def better():
    #return bestDescendant(0,0)
    #return 0
    x = 0
    for i in triangle[-1]:
        x = max(x,bestParent(len(triangle)-1,triangle[-1].index(i)))
    return x

print("The maximum sum from a path through the triangle is: %d" % better())
print("The true maximum sum from a path through the triangle is: %d" % brute())
