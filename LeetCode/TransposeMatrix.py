"""
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        columns = len(A)
        if columns == 0:
            return A
        rows = len(A[0])
        if rows == 0:
            return A
        returned = []
        for row in range(rows):
            returned += [[]]
            for col in range(columns):
                returned[row] += [A[col][row]]
        return returned

"""
My Solution:
Runtime: 64 ms, faster than 62.65% of Python3 online submissions for Transpose Matrix.
Memory Usage: 13.8 MB, less than 5.45% of Python3 online submissions for Transpose Matrix.
"""

"""
Fastest Solution (52ms):
class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        return [z for z in zip(*A)]

Smallest Memory (12688 kb):
class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        n = len(A)
        m = len(A[0])
        B = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(n):
            for j in range(m):
                B[j][i] = A[i][j]
        return B
"""
