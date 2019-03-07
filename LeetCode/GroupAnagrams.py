"""
Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ansdict = collections.defaultdict(list)
        for word in strs:
            key = sorted(word) #turn key of list into sorted str
            ansdict[''.join(key)].append(word)
        for k in ansdict:
            ans.append(ansdict[k])
        return ans

"""
My Solution
Runtime: 120 ms, faster than 68.09% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.2 MB, less than 28.10% of Python3 online submissions for Group Anagrams.
"""

"""
#Too Slow
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = set(s)
        for c in s_set:
            if s.count(c) != t.count(c):
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        for word in strs:
            matched = False
            for gramList in ans:
                if self.isAnagram(word,gramList[0]):
                    gramList.append(word)
                    matched = True
                    break
            if not matched:
                ans.append([word])
        return ans
"""

"""
Fastest Solution (100ms)
class Solution:
    def groupAnagrams(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[List[str]]
        '''
        mem = {}
        
        for s in strs:
            std = ''.join(sorted(s))
            if std in mem:
                mem[std] += [s]
            else:
                mem[std] = [s]
        return list(mem.values())
"""
