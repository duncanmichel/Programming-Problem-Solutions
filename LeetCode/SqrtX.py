"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:
Input: 4
Output: 2
Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        def isSqr(n,m):
            if m**2 == n:
                return True
            elif m**2 < n and (m+1)**2 > n:
                return True
            else:
                return False
        
        if x == 1:
            return 1
        
        y = int(x/2)
        ceiling = y
        
        while(True):
            if isSqr(x,y):
                return y
            elif y**2 > x:
                ceiling = min(y,ceiling)
                y = int(y/2)
                #print("[debug] decrease y to ",y,"ceiling:",ceiling)
            elif y**2 < x:
                y += int((ceiling-y)/2)
                #print("[debug] increase y to ",y,"ceiling:",ceiling)

"""
My Solution
Runtime: 132 ms, faster than 13.75% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.1 MB, less than 5.75% of Python3 online submissions for Sqrt(x).
"""

"""
Fastest Solution (48ms, but kind of cheating)
class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        return int(x**0.5)

Fastest Iterative Solution (56ms)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) >> 1
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                if mid == left:
                    return mid
                left = mid
            else:
                return mid
        return None
"""
