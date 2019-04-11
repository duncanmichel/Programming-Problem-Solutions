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
My Solution:

"""

"""
Fastest Solution:

"""
