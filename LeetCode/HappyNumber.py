"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the 
squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which 
does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        #I wanted to play with a reduce type format for this one
        def reduce(targetList,function,initialValue=0):
            runningValue = initialValue
            for item in targetList:
                runningValue = function(runningValue,item)
            return runningValue
        
        def iterate(num:int):
            digits = list(map(int,list(str(num))))
            #print ("reducing digits",digits)
            return reduce(digits,lambda a,b : a + b**2,0)
        
        total = n
        looped = {}
        while total != 1:# and total < 100000:
            total = iterate(total)
            #print("current total:",total)
            if total in looped:
                break
            else:
                looped[total] = True
        
        return total == 1

"""
My Solution:
Runtime: 44 ms, faster than 80.09% of Python3 online submissions for Happy Number.
Memory Usage: 13.1 MB, less than 5.29% of Python3 online submissions for Happy Number.
"""

"""
Fastest Solution (36ms):
class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            result = 0
            while n:
                result += (n % 10)**2
                n //= 10
            n = result
        return n == 1

Smallest Memory (12192 kb):
class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        return self.step(n, [])
        
    def step(self, n, prev) -> bool:
        s = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            s += digit * digit
            
        if s == 1:
            return True
        
        if s in prev:
            return False
        
        return self.step(s, prev + [s])
"""
