"""
Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a 
column that is different from the previous row's column by at most one.
Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.
Note:
1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

import math
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        size = len(A)
        memo = {}
        if size == 1:
            return A[0][0]
        
        #populate memo with values of path from the ground up
        for row_index in range(size-1,-1,-1):
            for col_index in range(0,size):
                memo_index = (row_index*size)+col_index
                if row_index == size-1: #lowest row
                    memo[memo_index] = A[row_index][col_index]
                #elif memo_index in memo.keys(): #path already evaluated
                    #pass
                else:
                    left_branch = ((row_index+1)*size)+max(0,col_index-1)
                    middle_branch = ((row_index+1)*size)+col_index
                    right_branch = ((row_index+1)*size)+min(size-1,col_index+1)
                    memo[memo_index] = A[row_index][col_index] + min(memo[left_branch],memo[middle_branch],memo[right_branch])
        
        #evaluate top row
        ans = math.inf
        for top_row_index in range(0,size):
            ans = min(ans,memo[top_row_index])
        
        return ans

"""
My Solution
Runtime: 88 ms, faster than 36.93% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 14.7 MB, less than 6.10% of Python3 online submissions for Minimum Falling Path Sum.
"""

"""
Fastest Solution (52ms):
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        ans = 0
        row = len(A)
        if row > 0:
            col = len(A[0])
            if col > 0:
                a = A[0]
                for i in range(1, row):
                    b = A[i][:]
                    for j in range(col):
                        x = a[j]
                        if j > 0 and a[j-1] < x:
                            x = a[j-1]
                        if j+1 < col and a[j+1] < x:
                            x = a[j+1]
                        b[j] += x
                    a = b
                ans = min(a)
        return ans
        
 Alt Fastest (56ms):
 class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        minpath = A[0]
        for i in range(1,len(A)):
            minpath.append(float('inf'))
            minpath = [A[i][j] + min(minpath[j-1],minpath[j],minpath[j+1]) for j in range(len(A[0])-1)]
            
        return min(minpath)
        
Smallest Memory Usage(12484 kb):
class Solution:
    def minFallingPathSum(self, A: 'List[List[int]]') -> 'int':
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0, i-1):min(len(row), i+2)])
        return min(A[0])
"""
