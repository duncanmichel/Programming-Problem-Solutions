"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:
Input: a = -2, b = 3
Output: 1
"""

class Solution(object):
    def getSum(self, a, b):
        def plus(x,y):
            carry = 0
            place = 1
            ans = 0
            while x > 0 and y > 0:
                xdigit = x%2
                ydigit = y%2
                thisdigit = xdigit^ydigit^carry
                carry = 1 if (xdigit & ydigit)|(xdigit & carry)|(ydigit & carry) else 0
                thisdigit *= place
                ans ^= thisdigit
                place <<= 1
                x //= 2
                y //= 2
            while x > 0:
                temp = (x%2 ^ carry) * place
                ans ^= temp
                place <<= 1
                carry = 1 if x%2 & carry else 0
                x //= 2
            while y > 0:
                temp = (y%2 ^ carry) * place
                ans ^= temp
                place <<= 1
                carry = 1 if y%2 & carry else 0
                y //= 2
            return ans
        
        def minus(x,y):
            return 0
        
        astr = bin(a)
        bstr = bin(b)
        if astr[0] == "-" and bstr[0] == "-":
            return -1 * plus(abs(a),abs(b))
        elif astr[0] == "-":
            if abs(a) > b:
                return -1 * minus(abs(a),b)
            else:
                return minus(b,abs(a))
        elif bstr[0] == "-":
            if abs(b) > a:
                return -1 * minus(abs(b),a)
            else:
                return minus(a,abs(b))
        
        return plus(a,b)

"""
MY Solution:

"""

"""
Fastest Solution ():


Smallest Memory ():

"""
