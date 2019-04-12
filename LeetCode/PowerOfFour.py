"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example 1:
Input: 16
Output: true
Example 2:
Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

#Because I just saw the power of three math solution, solving this was infinitely easier
class Solution(object):
    def isPowerOfFour(self, num):
        return num > 0 and (math.log10(num)/math.log10(4)).is_integer()

"""
My Solution:
Runtime: 24 ms, faster than 99.68% of Python online submissions for Power of Four.
Memory Usage: 11.7 MB, less than 6.41% of Python online submissions for Power of Four.
"""

"""
Fastest Solution (20ms):
class Solution(object):
    def isPowerOfFour(self, num):
        if( num > 0):
            if bin(num)[2:].count("1") == 1 and (bin(num)[2:][::-1].index('1')+1)%2 == 1:
                return True
        return False

Smallest Memory (10544 kb):
class Solution(object):
    def isPowerOfFour(self, num):
        if num==0:
            return False
        while num%4==0:
            num = num/4
        return num==1
"""
