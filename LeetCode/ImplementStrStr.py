"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

class Solution(object):
    def strStr(self, haystack, needle):
        return 0 if needle == "" else haystack.find(needle)

"""
My Solution:
Runtime: 20 ms, faster than 84.66% of Python online submissions for Implement strStr().
Memory Usage: 12.1 MB, less than 5.12% of Python online submissions for Implement strStr().
"""

#Algorithmic Solution [realizing if comparing to faster solutions that I'm doing unnecessary additional comparison
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        checkIndexStart = 0
        needleIndex = 0
        haystackIndex = 0
        while haystackIndex < len(haystack):
            #print("haystackIndex",haystackIndex,"needleIndex",needleIndex,"checkIndex",checkIndexStart)
            if needleIndex == len(needle):
                return checkIndexStart
            if haystack[haystackIndex] == needle[needleIndex]:
                if needleIndex == 0:
                    checkIndexStart = haystackIndex
                haystackIndex += 1
                needleIndex += 1
            elif needleIndex > 0:
                needleIndex = 0
                haystackIndex = checkIndexStart + 1
            else:
                haystackIndex += 1
        
        return checkIndexStart if needleIndex == len(needle) else -1
        
"""
My Solution:
Runtime: 32 ms, faster than 29.82% of Python online submissions for Implement strStr().
Memory Usage: 12 MB, less than 5.66% of Python online submissions for Implement strStr().
"""

"""
Fastest Solution (16ms):
class Solution(object):
    def strStr(self, haystack, needle):
        '''
        :type haystack: str
        :type needle: str
        :rtype: int
        '''
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
    
        return -1

Smallest Memory (10636 kb):
class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        
        n = len(needle)
        flag = False
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+n] == needle:
                flag = True
                break
        
        return i if flag else -1
"""
