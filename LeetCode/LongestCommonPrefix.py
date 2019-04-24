"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        listSize = len(strs)
        if listSize == 0:
            return ""
        
        lengths = [len(s) for s in strs]
        minStrLen = min(lengths)
        if minStrLen == 0:
            return ""
        
        prefixIndex = 0
        for strIndex in range(minStrLen):
            if [strs[i][strIndex] for i in range(listSize)].count(strs[0][strIndex]) == listSize:
                prefixIndex += 1
            else:
                break
        return strs[0][:prefixIndex]

"""
My Solution:
Runtime: 40 ms, faster than 73.39% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.2 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
"""

"""
Fastest Solution (28ms):
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        prefix = ''
        if not strs: return prefix
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for ch1,ch2 in zip(first,last):
            if ch1 == ch2:
                prefix += ch1
            else:
                break
        return prefix

Alt Fastest (32ms):
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs)==0 or '' in strs:
            return ''
        if len(set(strs))==1:
            return strs[0]
        maxlen=min([len(e) for e in strs])
        check = 1
        i=0
        while (check !=0 & i<maxlen):
            sub=[e[:i] for e in strs]
            if len(set(sub))==1:
                i+=1
            else:
                check = 0
        return strs[0][:i-1]

Smallest Memory (12224 kb):
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        
        longest = strs[0]
        for i in range(1, len(strs)):
            longest = self.shared_prefix(longest, strs[i])
            if longest == "":
                break

        return longest
            
    def shared_prefix(self, str1, str2):
        prefix_length = min(len(str1), len(str2))  # Assume it's as big as possible.
        for i, (char1, char2) in enumerate(zip(str1, str2)):
            if char1 != char2:
                prefix_length = i
                break
        return str1[:prefix_length]
"""
