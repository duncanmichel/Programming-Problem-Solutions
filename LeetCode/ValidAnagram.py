"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = set(s)
        for c in s_set:
            if s.count(c) != t.count(c):
                return False
        return True
"""
My Solution:
Runtime: 40 ms, faster than 98.52% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.3 MB, less than 26.30% of Python3 online submissions for Valid Anagram.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tlist = list(t)
        tlist.sort()
        slist = list(s)
        slist.sort()
        for i in range(0,len(slist)):
            if slist[i] != tlist[i]:
                return False
        return True     
"""
My Solution:
Runtime: 88 ms, faster than 22.98% of Python3 online submissions for Valid Anagram.
Memory Usage: 14 MB, less than 5.21% of Python3 online submissions for Valid Anagram.
"""
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tlist = list(t)
        for c in s:
            if c in tlist:
                #print("Removing",c,"from",tlist)
                tlist.remove(c)
            else:
                return False
        #print("Final list:",tlist)
        if tlist == []:
            return True
        else:
            return False
"""
My Solution:
Runtime: 1168 ms, faster than 5.32% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.7 MB, less than 5.21% of Python3 online submissions for Valid Anagram.
"""


"""
Fastest Solution:
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        if len(s) != len(t):
            return False
        alphabet = "abcdefghijklmnopqrstuvwxyz"  
        for i in alphabet:
            if s.count(i) != t.count(i):
                return False
        return True

Alt. Fastest Solution (same speed as my best):
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        return collections.Counter(s) == collections.Counter(t)

Best Memory Management:
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(s)):
            count1[ord(s[i]) - ord('a')] += 1
            count2[ord(t[i]) - ord('a')] += 1
        return count1 == count2
"""
