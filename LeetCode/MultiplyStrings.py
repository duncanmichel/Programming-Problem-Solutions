"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            lnum,snum,lsize,ssize = num1,num2,len(num1),len(num2)
        else:
            snum,lnum,ssize,lsize = num1,num2,len(num1),len(num2)
        convert = {48:0,49:1,50:2,51:3,52:4,53:5,54:6,55:7,56:8,57:9}
        ans = 0
        count = 0
        for sindex in range(ssize-1,-1,-1):
            #print("multiplying",snum[sindex],"by",lnum)
            temp = 0
            carry = 0
            coef = 1
            for lindex in range(lsize-1,-1,-1):
                product = convert[ord(snum[sindex])] * convert[ord(lnum[lindex])] + carry
                digit = product % 10
                carry = product // 10
                temp += digit * coef
                coef *= 10
                #print("product",product,"digit",digit,"carry",carry,"temp",temp,"coef",coef)
            carry *= coef
            ans += (temp + carry) * (10**count)
            count += 1
            #print("ans currently at",ans)
        return str(ans)

"""
My Solution:
Runtime: 124 ms, faster than 53.61% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.5 MB, less than 6.04% of Python3 online submissions for Multiply Strings.
"""

"""
Fastest Solution (40ms):
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert_num(n):
            s = 0
            for i in range(len(n)):
                s = s * 10 + int(n[i])
            return s
        
        return str(convert_num(num1) * convert_num(num2))
        
Alt Fastest (44ms):
class Solution:
    def translateToInt(self,ss: str) -> int:
        numTrans = {"0":0, "1":1, "2":2, "3":3, "4":4, '5':5, '6':6, '7':7, '8':8, '9':9}
        if len(ss)==1:
            return numTrans[ss]
        ii = 0 
        num = 0
        for char in ss[::-1]:
            if ii > 0:
                num += numTrans[char] * (pow(10,ii))
            else:
                num += numTrans[char]
            ii+=1
        return num
            
    def multiply(self, num1: str, num2: str) -> str:
        int1 = self.translateToInt(num1)    
        int2 = self.translateToInt(num2)
        return str(int1 * int2)
        
Smallest Memory (12236 kb):
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = [int(c) for c in num1][::-1]
        num2 = [int(c) for c in num2][::-1]
        ans = [0 for _ in range(len(num1) + len(num2) + 2)]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                ans[i + j] += n1 * n2
        
        for i in range(len(ans) - 1):
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        
        ans = ans[::-1]
        ind = 0
        while ind < len(ans) -1 and ans[ind] == 0:
            ind += 1
        
        
        return ''.join([str(c) for c in ans[ind:]])
"""
