"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with 
those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # for non-empty
        if s == "":
            return 0
        
        #dict of counts of each char
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        #add all even numbers, and the max even part of odds
        ans = 0
        odds = False
        for key in counts:
            if counts[key]%2 == 0:
                ans += counts[key]
            else:
                odds = True
                ans += counts[key] - 1
        #add an extra middle character if there was an odd count at all
        if odds:
            ans += 1
            
        #print("counts:",counts,", ans:",ans)        
        return ans

"""
My Solution
Runtime: 40 ms, faster than 71.34% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.2 MB, less than 6.31% of Python3 online submissions for Longest Palindrome.
"""

"""
Fastest Solution
class Solution:
    def longestPalindrome(self, s: 'str') -> 'int':
        ctr=collections.Counter(s)
        ans=0
        flag=0
        for a,c in ctr.items():
            if c&1==0:
                ans+=c
            else:
                ans+=c-1
                flag=1
        
        return ans+1 if flag else ans
"""
