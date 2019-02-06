"""
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x < 0:
            coeff = -1
            x = x * -1
        else:
            coeff = 1
        
        overflow = 2**31 - 1
        ans = 0
        while x > 0:
            ans *= 10
            n = x%10
            ans += n
            x = int((x-n)/10)
            if ans > overflow:
                return 0
        
        return ans*coeff
        
"""
My Solution
Runtime: 52 ms, faster than 92.59% of Python3 online submissions for Reverse Integer.
Memory Usage: 6.6 MB, less than 17.72% of Python3 online submissions for Reverse Integer.
"""

"""
Fastest Solution:
class Solution:
    def reverse(self, x: 'int') -> 'int':
    # Algo: Check if number positive or negative
    # If negative multiply reverse num by (-1) at end
    # Then, we need to continuously divide the number by 10 and
    # get the remainder to catch the digits
    # If the number is divisible, then remainder is 0, ignore this digit
    # Else capture the number
        if x == 0 or x <= -2**31 or x > 2**31 - 1:
            return 0
            
        revDigits = 0
        revNum = ""
        negative = False
        if x<0:
            negative = True
            x = x*(-1)

        while x>0:
            revDigits = x%10
            if revDigits == 0 and len(revNum)==0:
                pass
            else:
                revNum+= str(revDigits)
            x = int(x/10)
        
        revDigits = int(revNum)
        if negative == True and -1*revDigits> -2**31 and -1*revDigits< 2**31 -1:
            return -1*revDigits
        elif revDigits< 2**31 -1:
            return revDigits
        else:
            return 0
"""
