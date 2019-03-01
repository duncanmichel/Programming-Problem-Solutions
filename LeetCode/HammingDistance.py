"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        e = 0
        higher = max(x,y)
        ct = 0
        #print("starting x:",x,"starting y:",y,"starting ct:",ct)
        if ((2**e)<higher):
            while ((2**e)<higher):
                e += 1
            #e -= 1
        while (e>=0):
            #print("Running exponent:",e,"which is",2**e)
            if (x - 2**e) >= 0 and (y - 2**e) >= 0:
                x = x - 2**e
                y = y - 2**e
                #print("new x:",x,"new y:",y,"ct:",ct)
            elif (x - 2**e) >= 0:
                x = x - 2**e
                ct += 1
                #print("new x:",x,"y:",y,"ct:",ct)
            elif (y - 2**e) >= 0:
                y = y - 2**e
                ct += 1
                #print("x:",x,"new y:",y,"ct:",ct)
            e-= 1
        return ct

"""
My Solution:
Runtime: 40 ms, faster than 47.57% of Python3 online submissions for Hamming Distance.
Memory Usage: 13.3 MB, less than 5.84% of Python3 online submissions for Hamming Distance.
"""

"""
Fastest Solution:
class Solution:
    def hammingDistance(self,x: 'int', y: 'int') -> 'int': 
        a=bin(x).lstrip('0b')        
        b=bin(y).lstrip('0b')        
        q=0
        if len(a)<len(b):
            t=a.rjust(len(b),'0')        
            for i in range(0,len(t)):
                if t[i]!=b[i]:
                    q=q+1
        elif len(a)>len(b):
            t=b.rjust(len(a),'0')
            for i in range(0,len(t)):
                if t[i]!=a[i]:
                    q=q+1
        elif len(a)==len(b):
            for i in range(0,len(a)):
                if a[i]!=b[i]:
                    q=q+1       
        return(q)

Smallest Solution (in memory):
class Solution:
    def hammingDistance(self, x, y):
        '''
        :type x: int
        :type y: int
        :rtype: int
        '''
        def cverto2(x):
            lst = []
            while x > 0:
                rem = x % 2
                lst.append(rem)
                x = x//2
            return lst
        
        xlst = cverto2(x)
        ylst = cverto2(y)
        while len(xlst) > len(ylst):
            ylst.append(0)
        
        while len(ylst) > len(xlst):
            xlst.append(0)
        
        ct = 0
        for idx in range(len(xlst)):
            if xlst[idx] != ylst[idx]:
                ct += 1
        return ct
"""
