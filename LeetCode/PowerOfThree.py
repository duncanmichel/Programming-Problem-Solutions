"""
Given an integer, write a function to determine if it is a power of three.
Example 1:
Input: 27
Output: true
Example 2:
Input: 0
Output: false
Example 3:
Input: 9
Output: true
Example 4:
Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        n = float(n)
        while n > 3.0:
            n = float(n/3)
        return True if n == 3.0 else False

"""
My Solution:
Runtime: 148 ms, faster than 59.24% of Python online submissions for Power of Three.
Memory Usage: 11.8 MB, less than 5.29% of Python online submissions for Power of Three.
"""

"""
Fastest Solution (116ms):
class Solution(object):
    def isPowerOfThree(self, n):
        if n==0:
            return False
        while n%3==0:
            n = n/3
        return n==1

Alt Fastest Solution (128ms) [math solution, no loops]:
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        temp = math.log10(n) / math.log10(3)
        if temp.is_integer():
            return True
        return False

(132ms):
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and n == 3**round(log(n,3))

Smallest Memory (10516 kb):
class Solution(object):
    def isPowerOfThree(self, n):
        if n==0:
            return False
        if n==1:
            return True
        if n%3!=0:
            return False
        if n//3==1:
            return True
        return self.isPowerOfThree(n//3)
"""
