"""
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        generator, triangle = {i:0 for i in range(numRows)},[]
        generator[0] = 1
        
        for rowIndex in range(numRows):
            old_col,row = 0,[]
            for column in range(rowIndex+1):
                val = old_col + generator[column]
                row += [val]
                old_col = generator[column]
                generator[column] = val
            triangle += [row]
        return triangle

"""
My Solution:
Runtime: 36 ms, faster than 75.75% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13 MB, less than 5.83% of Python3 online submissions for Pascal's Triangle.
"""

"""
Fastest Solution (28ms):
class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0: return []
        
        pascal = []
        mat = [[0] * numRows for i in range(numRows)]

        for i in range(0, numRows):
            for j in range(0, numRows):
                if i == j or j == 0:
                    mat[i][j] = 1
                elif i > 0:
                    mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
        
            pascal.append(mat[i][:i+1])
        
        return pascal

Smallest Memory (12176 kb):
class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        res = [[1],[1,1]]
        i = 3
        while i <= numRows:
            self.addToList(res, i)
            i += 1
        return res
    
    def addToList(self, res, numRows):
        r = []
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                r.append(1)
            else:
                r.append(res[-1][i-1]+res[-1][i])
        res.append(r)
"""
