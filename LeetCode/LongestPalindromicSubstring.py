"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            if len(string) > 2:
                return True
            return isPalindrome(string[1:len(string)-1]) if string[0]==string[-1] else False
        
        if len(s) < 2:
            return s
        
        substring = s[0]
        sslen = 1
        size,lastIndex = len(s),len(s)-1
        for index in range(size): #for each char, bubble up as long as palindromes are found
            startIndex,endIndex = index-1,index+1 #start on either side [start][index][end]
            while startIndex >= 0 and endIndex <= lastIndex and s[startIndex]==s[endIndex]:  
                #print("palindrome: ",s[startIndex:endIndex+1])
                startIndex -= 1
                endIndex += 1
            if len(s[startIndex+1:endIndex]) > sslen:
                #print("Better palindrome than",substring,"found: ",s[startIndex+1:endIndex])
                substring = s[startIndex+1:endIndex]
                sslen = len(substring)
                
            startIndex,endIndex = index,index+1 #start with two characters [index][next]
            while startIndex >= 0 and endIndex <= lastIndex and s[startIndex]==s[endIndex]:
                #print("palindrome: ",s[startIndex:endIndex])
                startIndex -= 1
                endIndex += 1 
            if len(s[startIndex+1:endIndex]) > sslen:
                #print("Better palindrome than",substring,"found: ",s[startIndex+1:endIndex])
                substring = s[startIndex+1:endIndex]
                sslen = len(substring)
                
        return substring

"""
My Solution:
Runtime: 736 ms, faster than 84.86% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.2 MB, less than 25.10% of Python3 online submissions for Longest Palindromic Substring.
"""

"""
Fastest Solution (48ms):
class Solution:
    def longestPalindrome(self, s):
        maxlen,begin=1,0
        if len(s)<2 or s==s[::-1]:
            return s
        for i in range(1,len(s)):
            odd=s[i-maxlen-1:i+1]
            even=s[i-maxlen:i+1]
            
            if i-maxlen>=1 and odd==odd[::-1]:
                begin=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                begin=i-maxlen
                maxlen+=1
        return s[begin:begin+maxlen]

Smallest Memory (12120 kb):
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen) // 2 : (centerIndex  + maxLen) // 2]
"""
