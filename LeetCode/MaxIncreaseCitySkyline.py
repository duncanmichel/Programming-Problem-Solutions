"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
What is the maximum total sum that the height of the buildings can be increased?
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
Notes:
1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        size = len(grid)
        row_max = {}
        col_max = {}
        
        #fill out the two hashmaps
        for row in range(size):
            for col in range(size):
                if col in col_max.keys():
                    col_max[col] = max(grid[row][col],col_max[col])
                else:
                    col_max[col] = grid[row][col]
                if row in row_max.keys():
                    row_max[row] = max(grid[row][col],row_max[row])
                else:
                    row_max[row] = grid[row][col]
        
        #get the sum of the best heights
        answer = 0
        for row in range(size):
            for col in range(size):
                target = min(row_max[row],col_max[col])
                answer += target - grid[row][col]
                #print("answer is now",answer)
        
        #print (grid)
        return answer

"""
My Solution:
Runtime: 60 ms, faster than 36.78% of Python3 online submissions for Max Increase to Keep City Skyline.
Memory Usage: 13.1 MB, less than 5.55% of Python3 online submissions for Max Increase to Keep City Skyline.
"""

"""
Fastest Solution (40ms):
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        maxVert = []
        maxHoriz = []
        for vert in grid:
            maxVert.append(max(vert))
        
        transposedGrid = list(zip(*grid))
        for horizontal in transposedGrid:
            maxHoriz.append(max(horizontal))
        
        #print(maxVert)
        #print(maxHoriz)
        
        sumTotal = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                #print("At point ("+str(x)+','+str(y)+') max is ' + str(min(maxHoriz[x],maxVert[y])))
                #print(str(x)+ ' max in x: ' + str(maxHoriz[x]))
                #print(str(y)+ ' max in y: ' + str(maxVert[y]))
                diff = min(maxHoriz[x],maxVert[y]) - grid[y][x]                
                sumTotal+=diff

        return sumTotal

Smallest Memory (12304 kb):
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        n = len(grid)
        horizontal = list(map(max, grid))
        vertical = list(map(max, zip(*grid)))
        
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(horizontal[i], vertical[j]) - grid[i][j]
        return res
"""
