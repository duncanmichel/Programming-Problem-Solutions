"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121
Output: true
Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:
Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        size = 0
        num = x
        while num > 0:
            size += 1
            num //= 10
        stack,middle,odd = [],size//2,True if size%2==1 else False
        #print('size',size,'middle',middle,'odd',odd)
        for i in range(size):
            if i < middle:
                stack.append(x%10)
            elif i == middle and odd:
                #print("got to odd condition on index",i,"x is ",x)
                pass
            else:
                if stack.pop() != x%10: return False
            x //= 10
        return True

"""
My Solution:
Runtime: 112 ms, faster than 75.59% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.2 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
"""


"""
Fastest Solution (76ms) [cheating]:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

Alt Fastest (84ms):
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while x > y: 
            y = y * 10 + x % 10
            x = x // 10
        answer = (y == x or y // 10 ==x) 
        return answer

Smallest Memory (12392 kb):
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x%10 == 0:
            return False
        else:
            
            def rev(x):
                reverse = 0
                temp = x
                while temp != 0:
                    reverse = reverse*10 + temp%10
                    temp = temp//10
                return reverse

            print(x)
            print(rev(x))
            return x == rev(x)
"""
