"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single 
digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution(object):
    def plusOne(self, digits):
        if digits == [0]:
            return [1]
        lastIndex = len(digits)-1
        carry = 1
        for index in range(lastIndex,-1,-1):
            newVal = digits[index] + carry
            digits[index] += carry if newVal < 10 else -digits[index]
            carry = 0 if newVal < 10 else 1
            if not carry:
                break
        return [1]+digits if carry else digits

"""
My Solution:
Runtime: 20 ms, faster than 96.45% of Python online submissions for Plus One.
Memory Usage: 11.7 MB, less than 5.30% of Python online submissions for Plus One.
"""

"""
Fastest Solution (16ms):
class Solution:
    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        if not digits:
            return digits
        ret = [0]*len(digits)
        carry = 1        
        for i in range(len(digits)-1,-1,-1): 
            ret[i]= (digits[i] + carry)%10
            carry = (digits[i] + carry)/10
        
        if carry == 1:
            return [1] + ret
        else:        
            return ret

Smallest Memory (10440 kb):
class Solution(object):
    def plusOne(self, digits):
        flag = True
        for i in range(len(digits)-1,-1,-1):
            if flag:
                if digits[i]==9:
                    digits[i] = 0
                    flag = True
                else:
                    digits[i] += 1
                    flag = False
            else:
                break
        if flag:
            digits=[1]+digits
        return digits
"""
