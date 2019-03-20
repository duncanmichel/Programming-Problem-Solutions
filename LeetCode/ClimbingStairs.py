"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def memoizeStairs(x):
            if x in memo.keys():
                return memo[x]
            elif x == 1:
                memo[x] = 1
                return 1
            elif x == 2:
                memo[x] = 2
                return 2
            else:
                memo[x] = memoizeStairs(x-2) + memoizeStairs(x-1)
                return memo[x]
        return memoizeStairs(n)

"""
My Solution:
Runtime: 36 ms, faster than 61.82% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.2 MB, less than 5.18% of Python3 online submissions for Climbing Stairs.
"""

"""
Fastest Solution (28ms):
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 1:
            return 1

        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1

        for stair in range(2, n + 1):
            table[stair] = table[stair - 1] + table[stair - 2]

        return table[n]
"""