"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false
Example 4:
Input: "([)]"
Output: false
Example 5:
Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        openParen = "([{"
        closeParen = ")]}"
        stack = []
        
        for char in s:
            if char in openParen:
                stack.append(char)
            else:
                if len(stack)==0 or not closeParen.find(char) == openParen.find(stack.pop()):
                    return False
        return len(stack)==0

"""
My Solution:
Runtime: 36 ms, faster than 87.17% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
"""

"""
Fastest Solution (28ms):
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        op = '({['
        cp = ')}]'
        cp_to_op = {')': '(',
                   '}': '{',
                   ']': '['}
        paren = list()
        
        for c in s:
            if c in op:
                paren.append(c)
            elif c in cp:
                if len(paren) == 0:
                    return False
                if cp_to_op[c] != paren.pop():
                    return False
        if len(paren) > 0:
            return False
        else:
            return True

Smallest Memory (12128 kb):
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        dictt = {')': '(',
                ']' : '[',
                '}' : '{'}
        que = ''
        i = 0
        while i < len(s):
            if s[i] in dictt:
                if que == '':
                    return False
                elif que[-1] == dictt[s[i]]:
                    que = que[:-1]
                    i += 1
                else:
                    return False
            else:
                que += s[i]
                i += 1
        if que == '':
            return True
        return False
"""
