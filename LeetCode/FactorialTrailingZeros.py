"""
Given an integer n, return the number of trailing zeroes in n!.
Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
"""
#https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
#https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52399/My-python-solution-in-O(1)-space-O(logN)-time

#Algorithmically accurate, but too slow
class Solution:
    def trailingZeroes(self, n: int) -> int:
        tens,fives,twos = 0,0,0
        while n > 1:
            if n%10==0: 
                temp = n
                while temp%10 == 0:
                    tens += 1
                    temp //= 10
                while temp%5 == 0:
                    fives += 1
                    temp //= 5
                n-= 5                
            elif n%5 == 0:
                temp = n
                while temp%5 == 0:
                    fives += 1
                    temp //= 5
                n-= 5
            else:
                n -= 1
        #print("tens",tens,"fives",fives)
        return tens + fives

"""
My Solution:

"""

"""
Fastest Solution ():


Smallest Memory ():

"""
