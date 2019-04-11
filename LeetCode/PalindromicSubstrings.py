"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""

#Working! I realized that I don't have to keep checking the entire string if all but the outer two characters
#contain a valid palindrome
class Solution:        
    def countSubstrings(self, s: str) -> int:
        count,lastIndex = len(s),len(s)-1
        for index in range(count): #for each char, bubble up as long as palindromes are found
            startIndex,endIndex = index-1,index+1 #start on either side [start][index][end]
            while startIndex >= 0 and endIndex <= lastIndex and s[startIndex]==s[endIndex]:       
                count += 1
                startIndex -= 1
                endIndex += 1
            startIndex,endIndex = index,index+1 #start with two characters [index][next]
            while startIndex >= 0 and endIndex <= lastIndex and s[startIndex]==s[endIndex]:
                count += 1
                startIndex -= 1
                endIndex += 1       
        return count

"""
My Solution:
Runtime: 116 ms, faster than 89.13% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 13.2 MB, less than 33.54% of Python3 online submissions for Palindromic Substrings.
"""
    
#Passes 128/130 tests, but fails on large input
class Solution:
    def isPalindrome(self,test_str:str):
        stack,size = [],len(test_str) 
        halfway,odd = size//2, size%2 == 1
        if size is 1:
            return True
        for char_index in range(size):
            if char_index < halfway:
                stack.append(test_str[char_index])
            elif char_index == halfway and odd:
                pass
            else:
                if stack.pop() != test_str[char_index]:
                    return False
        return True
    
    def countSubstrings(self, s: str) -> int:
        startIndex,endIndex,lastIndex,size = 0,1,len(s)-1,len(s)
        count = size
        if size == 0:
            return 0
        if size == 1:
            return 1
        for index in range(size): #for each char, bubble up as long as palindromes are found
            startIndex,endIndex = index-1,index+1 #start on either side [start][index][end]
            while startIndex >= 0 and endIndex <= lastIndex and self.isPalindrome(s[startIndex:endIndex+1]):       
                count += 1
                #print("found",s[startIndex:endIndex+1],"count now",count,"index",index)
                startIndex -= 1
                endIndex += 1
            startIndex,endIndex = index,index+1 #start with two characters [index][next]
            while startIndex >= 0 and endIndex <= lastIndex and self.isPalindrome(s[startIndex:endIndex+1]):
                count += 1
                #print("found",s[startIndex:endIndex+1],"count now",count,"index",index)
                startIndex -= 1
                endIndex += 1
        
        return count
    
#Passes 128/130 tests, but fails on large input   
class Solution:
    def isPalindrome(self,test_str:str):
        stack,size = [],len(test_str) 
        odd = size%2 == 1
        halfway = size//2
        #print("size is ",size,"halfway is ",halfway,"odd is ",odd)
        if size is 1:
            return True
        for char_index in range(size):
            if char_index < halfway:
                #print('\t[check] appending',test_str[char_index])
                stack.append(test_str[char_index])
            elif char_index == halfway and odd:
                #print('\t[check] ignoring',test_str[char_index])
                pass
            else:
                #print('\t[check] comparing',test_str[char_index],'to top of stack')
                if stack.pop() != test_str[char_index]:
                    return False
        return True
    
    def countSubstrings(self, s: str) -> int:
        count,startIndex,endIndex,lastIndex,size = 0,0,1,len(s)-1,len(s)
        if size == 0:
            return 0
        if size == 1:
            #print("single string",s)
            return 1
        while startIndex < endIndex: #check all substrings by incrementing endIndex to the end, then incrementing startIndex there
            #print("string",s[startIndex:endIndex],"from",startIndex,"to",endIndex)#,"is", self.isPalindrome(s[startIndex:endIndex]))
            count += 1 if self.isPalindrome(s[startIndex:endIndex]) else 0
            startIndex += 1 if endIndex == size else 0
            endIndex += 1 if endIndex < size else 0

        return count + self.countSubstrings(s[1:lastIndex]) #add count to all substrings one in.

#Fails at 22/130 tests due to taking too long        
    def countSubstrings(self, s: str) -> int:
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        elif self.isPalindrome(s):
            return 1 + self.countSubstrings(s[1:]) + self.countSubstrings(s[:len(s)-1]) - self.countSubstrings(s[1:len(s)-1])
        else:
            return 0 + self.countSubstrings(s[1:]) + self.countSubstrings(s[:len(s)-1]) - self.countSubstrings(s[1:len(s)-1])



"""
Fastest Solution (36ms):
class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        if not s:
            return 0
        res = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            res += (j-i) * (j-i+1) // 2
            left = i - 1
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            i = j
        return res
        
Smallest Memory (12180 kb):
class Solution:
    # This approach uses an inward outward approach for finding all the palindromes in a substring
    def countSubstrings(self, s: 'str') -> 'int':
        N = len(s)
        ans = 0 
        
        # There are 2N - 1 center, N for the letter in the string plus N - 1 for the 
        # spaces in between each string
        for center in range(2*len(s) - 1):
            left = int(center / 2) # compute the left index
            right = left + center % 2 # if center is even the right will be equal to the left
                                      # other wise the right index will be offset by one
            
            while left >= 0 and right < N and s[left] == s[right]: # check if indexes are out of bounds
                                                                    # and makes sure the character on both sides
                                                                    # of the center are equal
                ans += 1
                left -= 1
                right += 1
        return ans
            
            
    def countSubstrings2(self, s: 'str') -> 'int':
        
        count = 0
        #print(s[0:3])
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                rev_s = ''.join(reversed(s[i:j]))
                if s[i:j] == rev_s:
                    count += 1
        
        return count
"""
