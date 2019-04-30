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

class Solution(object):
    def trailingZeroes(self, n):        
        ans = 0
        while n > 0:
            ans += n//5
            n //= 5
        return ans

"""
My Solution:
Runtime: 24 ms, faster than 63.49% of Python online submissions for Factorial Trailing Zeroes.
Memory Usage: 11.7 MB, less than 5.21% of Python online submissions for Factorial Trailing Zeroes.
"""

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
#memoization solution, not working yet
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num,tens,fives,count = 2,0,0,0
        memo = {}
        while num <= n:
            temp = num
            print("checking",num,"", end='')
            if num%10==0: 
                check = True
                count = 0
                while temp%10 == 0:
                    if temp in memo:
                        print("memo check in tens",temp)
                        tens += 1 + memo[temp][0]
                        #fives += memo[temp][1] ???
                        count = 0
                        check = False
                        break
                    count += 1
                    #tens += 1
                    temp //= 10
                tens += count
                while check and temp%5 == 0:
                    fives += 1
                    temp //= 5
                memo[num] = (tens, fives)
                num += 5                
            elif num%5 == 0:
                count = 0
                while temp%5 == 0:
                    if temp in memo:
                        print("memo check in fives",temp)
                        fives += 1 + memo[temp][1]
                        count = 0
                        break
                    count += 1
                    #fives += 1
                    temp //= 5
                fives += count
                memo[num] = (tens, fives)
                num += 5
            else:
                num += 1
            print("tens",tens,"fives",fives)
        #print("tens",tens,"fives",fives)
        return tens+fives
"""

"""
Fastest Solution (20ms):
[20ms submission of same solution]

Smallest Memory (10468 kb):
class Solution(object):
    def trailingZeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
"""
