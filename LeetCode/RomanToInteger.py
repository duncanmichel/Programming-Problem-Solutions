"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I":1,"V":5,"X": 10,"L":50,"C":100,"D":500,"M":1000}
        index = 0
        val = 0
        for n in s:
            if s[index:index+2] in ["IV","IX","XL","XC","CD","CM"]:
                val -= rom[n]
            else:
                val += rom[n]
            index += 1
        return val
        
"""
My Solution:
Runtime: 132 ms, faster than 64.37% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.5 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
"""

"""
Fastest Solution:
class Solution:
    def romanToInt(self, os: 'str') -> 'int':
        x = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000}
        s = 0
        prev = None
        cur = None
        
        for cur_s in os:
            cur = x[cur_s]
            if prev is None:
                prev = cur
            elif prev >= cur:
                s = s + prev
                prev = cur
            else:
                s = s + (cur - prev)
                prev = None
                cur = None
        if cur is not None:
            s = s + cur
        return s

Next Fastest:
class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        ans = 0
        if 'IV' in s:
            ans -= 2
        if 'IX' in s:
            ans -= 2
        if 'XL' in s:
            ans -= 20
        if 'XC' in s:
            ans -= 20
        if 'CD' in s:
            ans -= 200
        if 'CM' in s:
            ans -= 200
            
        for c in s:
            if c == 'I':
                ans += 1
            elif c == 'V':
                ans += 5
            elif c == 'X':
                ans += 10
            elif c == 'L':
                ans += 50
            elif c == 'C':
                ans += 100
            elif c == 'D':
                ans += 500
            elif c == 'M':
                ans += 1000
                
        return ans
"""
