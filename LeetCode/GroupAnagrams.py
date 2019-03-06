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
My Solution

"""

"""
Fastest Solution

"""
