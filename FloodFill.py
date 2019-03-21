"""
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

                                {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };

                        x=4, y=4, color=3 

                               {{1, 1, 1, 1, 1, 1, 1, 1},
                     {1, 1, 1, 1, 1, 1, 0, 0},
                     {1, 0, 0, 1, 1, 0, 1, 1}, 
                     {1, 3, 3, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 3, 3, 0},
                     {1, 1, 1, 1, 1, 3, 1, 1},
                     {1, 1, 1, 1, 1, 3, 3, 1}, };


Note: Use zero based indexing.


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains Two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix. Then in the next line are three values x, y and K.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=100
1<=M[][]<=100

Example:
Input:
3
3 4
0 1 1 0 1 1 1 1 0 1 2 3
0 1 5
2 2
1 1 1 1
0 1 8
4 4 
1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4
0 2 9

Output:
0 5 5 0 5 5 5 5 0 5 2 3
8 8 8 8
1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4

"""

#code
def printMap(row:int,col:int,pixels:list):
    upperBound = col
    lowerBound = 0
    for i in range(0,row):
        print(pixels[lowerBound:upperBound])
        lowerBound = upperBound
        upperBound += col

def floodFill():
    [row,col] = list(map(int,input().split()))
    pixelMap = list(map(int,input().split()))
    [x,y,newColor] = list(map(int,input().split()))
    oldColor = pixelMap[(x*col)+y]
    #isChanged = [False]*len(pixelMap)
    
    def recursiveFill(x:int,y:int):
        #print("Recursively checking x",x,"y",y,"cur Color",pixelMap[(x*col)+y])#,"isChanged",isChanged[(x*col)+y])
        if pixelMap[(x*col)+y] == oldColor: #(not isChanged[(x*col)+y]) and pixelMap[(x*col)+y] == oldColor:
            pixelMap[(x*col)+y] = newColor
            #isChanged[(x*col)+y] = True
            if x+1 < row:
                recursiveFill(x+1,y)
            if x-1 >= 0:
                recursiveFill(x-1,y)
            if y+1 < col:
                recursiveFill(x,y+1)
            if y-1 >= 0:
                recursiveFill(x,y-1)
    
    #pixelMap[(x*(col))+y] = newColor
    recursiveFill(x,y)
    
    print("Answer for case ",test_case)
    #printMap(row,col,pixelMap)
    print(" ".join(map(str,pixelMap)))

num_test_cases = int(input())

for test_case in range(0,num_test_cases):
    floodFill()


"""
#Not working. I think I'm running into a problem with the truth table, possibly due to multiple accesses to the same array recursively
def generatePixels(col:int,row:int,starter:list):
    newMap = []
    lowerBound = 0
    for x in range(0,col):
        upperBound = lowerBound + row
        newMap.append(starter[lowerBound:upperBound])
        lowerBound = upperBound
        upperBound += row
    return newMap

def generateTruthMap(col:int,row:int):
    return [[False]*row]*col

'''
def recursiveFill(x:int,y:int,oldColor:int,newColor:int,pixels:list):
    if pixels == None or pixels[x] == None:
        print("pixels becomes unstable")
        return pixels
    try:
        if pixels[x][y] == oldColor:
            pixels[x][y] = newColor
            print("Successfully filled x",x,"y",y)
            if x+1 < len(pixels):
                pixels = recursiveFill(x+1,y,oldColor,newColor,pixels)
            if x-1 >= 0:
                pixels = recursiveFill(x-1,y,oldColor,newColor,pixels)
            if y+1 < len(pixels[x]):
                pixels = recursiveFill(x,y+1,oldColor,newColor,pixels)
            if y-1 >= 0:
                pixels = recursiveFill(x,y-1,oldColor,newColor,pixels)
        else:
            return pixels
    except Exception as e:
        print("Failed to fill pixel x:"+str(x)+" y:"+str(y)+" with ERROR:"+ str(e))
'''        


def solve():
    [col,row] = list(map(int,input().split()))
    initialList = list(map(int,input().split()))
    [x,y,newColor] = list(map(int,input().split()))
    pixelMap = generatePixels(col,row,initialList)
    isChanged = generateTruthMap(col,row)
    oldColor = pixelMap[x][y]
    
    def recursiveFill(x:int,y:int):
        print("Recursively checking x",x,"y",y,"isChanged",isChanged[x][y],"cur Color",pixelMap[x][y])
        if (not isChanged[x][y]) and pixelMap[x][y] == oldColor:
            pixelMap[x][y] = newColor
            isChanged[x][y] = True
            if x+1 < len(pixelMap):
                recursiveFill(x+1,y)
            if x-1 >= 0:
                recursiveFill(x-1,y)
            if y+1 < len(pixelMap[x]):
                recursiveFill(x,y+1)
            if y-1 >= 0:
                recursiveFill(x,y-1)
                
    recursiveFill(x,y)
    
    print("Answer for case ",test_case)
    for line in pixelMap:
        print(line)

num_test_cases = int(input())

for test_case in range(0,num_test_cases):
    solve()
"""
