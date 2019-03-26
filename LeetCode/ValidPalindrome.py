"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        frontIndex = 0
        lastIndex = len(s) - 1
        
        while lastIndex >= frontIndex:
            while not (s[lastIndex].lower() in alphabet) and lastIndex >= frontIndex:
                lastIndex -= 1
            while not (s[frontIndex].lower() in alphabet) and lastIndex >= frontIndex:
                frontIndex +=1
            if lastIndex >= frontIndex:
                if s[lastIndex].lower() != s[frontIndex].lower():
                    return False
                lastIndex -= 1
                frontIndex +=1
            else:
                break
                
        return True

"""
My Solution:
Runtime: 64 ms, faster than 69.31% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.3 MB, less than 42.33% of Python3 online submissions for Valid Palindrome.
"""

"""
Fastest Solution (44ms):
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s_new = re.sub('[^a-zA-Z0-9]', '', s)
        s_rev = s_new[::-1]
        return s_new.lower() == s_rev.lower()

Smallest Memory (12336 kb):
import string
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s= s.lower()
        a=''
        for x in s:
            if x not in string.punctuation and x not in string.whitespace:
                a += x
        #a = [x for x in s if x not in string.punctuation and x not in string.whitespace]
        return a == a[::-1]
"""
