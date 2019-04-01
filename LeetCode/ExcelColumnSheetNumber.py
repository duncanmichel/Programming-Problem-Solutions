"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:
Input: "A"
Output: 1
Example 2:
Input: "AB"
Output: 28
Example 3:
Input: "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = "aABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphanum = [i for i in range(28)]
        translate = dict(zip(alpha,alphanum))
        
        column = 0
        for char in s:
            column += (column * 26) + translate[char] - column
        
        return column

"""
My Solution:
Runtime: 60 ms, faster than 44.38% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.5 MB, less than 5.44% of Python3 online submissions for Excel Sheet Column Number.
"""

"""
Fastest Solution (40ms):
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        n = len(s) - 1
        for i, letter in enumerate(s):
            res += (ord(letter) - ord('A') + 1) * pow(26, n - i)
        return res

Smallest Memory (12300 kb):
class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        letters = list(string.ascii_uppercase)
        d = dict((e, i+1) for i, e in enumerate(letters))
        num = 0
        s = list(s)
        pos = 1
        while(s):
            num+=d[s.pop()]*pos
            pos = pos*26
            
        return num
"""
