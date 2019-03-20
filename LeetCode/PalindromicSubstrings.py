"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""

#Fails "aba" test
class Solution:
    def isPalindrome(self,test_str:str):
        stack = []
        for char_index in range(0,len(test_str)):
            if char_index < len(test_str)/2:
                stack.append(test_str[char_index])
            elif char_index == len(test_str)/2 and len(test_str)%2 != 0:
                pass
            else:
                if stack.pop() != test_str[char_index]:
                    return False
        return True
        
    def countSubstrings(self, s: str) -> int:
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        elif self.isPalindrome(s):
            return 1 + self.countSubstrings(s[1:]) + self.countSubstrings(s[:len(s)-1]) - self.countSubstrings(s[1:len(s)-1])
        else:
            return 0 + self.countSubstrings(s[1:]) + self.countSubstrings(s[:len(s)-1]) - self.countSubstrings(s[1:len(s)-1])

"""
My Solution:

"""

"""
Fastest Solution:

"""
