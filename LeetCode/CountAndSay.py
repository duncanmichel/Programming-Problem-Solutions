"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
Example 1:
Input: 1
Output: "1"
Example 2:
Input: 4
Output: "1211"
        validTests = 
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211


"""

class Solution:
    
    def countAndSay(self, n: int) -> str:

"""
        memo = {}
        def nextSay(prevStr:str) -> str:
            nextStr = ""
            if prevStr == nextStr: #0 -> 1 case
                return "1"
            count = 0
            curChar = prevStr[0]
            for char in prevStr:
                if char == curChar:
                    count += 1
                else:
                    nextStr += str(count)+curChar
                    curChar = char
                    count = 1
            
            return nextStr + str(count)+curChar
        
        retStr = ""
        for i in range(n):
            if i in memo:
                retStr = memo[i]
            else:
                memo[i] = retStr = nextSay(retStr)
                #print (retStr)
        #print (validTests)
        return retStr

"""
My Solution:
Runtime: 40 ms, faster than 81.26% of Python3 online submissions for Count and Say.
Memory Usage: 13.3 MB, less than 5.11% of Python3 online submissions for Count and Say.
"""

"""
Fastest Solution (32ms):
class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s

Smallest Memory (12104 kb):
[same as fastest]
"""
