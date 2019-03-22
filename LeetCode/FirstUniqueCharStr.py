"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        def checkUnique(char:str,remaining:str):
            for c in remaining:
                if c == char:
                    return False
            return True
        
        tgt_index = -1
        
        if s == "":
            return tgt_index
        elif len(s) < 2:
            return 0
        
        found = []
        for index in range(0,len(s)):
            if (s[index] not in found) and (checkUnique(s[index],s[index+1:])):
                return index
            else:
                found.append(s[index])
            
        
        return tgt_index

"""
My Solution:
Runtime: 172 ms, faster than 29.89% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.3 MB, less than 5.04% of Python3 online submissions for First Unique Character in a String.
"""

"""
Fastest Solution (36ms):
class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        alphabet, ans = 'abcdefghijklmnopqrstuvwxyz', float('inf')
        for c in alphabet:
            i = s.find(c)
            if i == -1:
                continue
            j = s.find(c, i + 1)
            if j == -1:
                ans = min(ans, i)
        return ans if ans != float('inf') else -1

Alt Fastest (108ms) [algorithmic solution]:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for n in range(len(s)):
            if s[n] in table:
                table[s[n]] = -1
            else:
                table[s[n]] = n

        min = len(s)
        for key in table:
            if table[key] != -1:
                if table[key] < min:
                    min = table[key]

        if min != len(s):
            return min
        else:
            return -1
            
Alt Fastest (96ms) [python Enumerate, but good algo otherwise]:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        seen = set()
        for idx,c in enumerate(s):
            if c not in seen:
                seen.add(c)
                hashmap[c] = idx
            elif c in hashmap:
                hashmap.pop(c) 
        
        return min(hashmap.values()) if hashmap else -1

Smallest Memory (12264 kb):
class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        count_map = {}
        for i in s:
            if i in count_map:
                count_map[i] += 1
            else:
                count_map[i] = 1
        for key, value in count_map.items():
            if value == 1:
                return s.index(key)
        return -1
"""
