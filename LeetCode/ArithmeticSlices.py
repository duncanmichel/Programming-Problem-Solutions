"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive 
elements is the same.
For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.
1, 1, 2, 5, 7
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
The function should return the number of arithmetic slices in the array A.
Example:
A = [1, 2, 3, 4]
return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

#runtime: O[N] because it is a single pass through the array. Constant space because no helper arrays required
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        size = len(A)
        ans = 0
        
        #didn't actually need this method, but was a good way to start thinking about the code
        def isArithmeticSlice(interval:int,start:int,end:int):
            if end-start < 3 or start < 0 or end >= size:
                return False
            for index in range(start+1,end+1):
                if A[index] - A[index-1] != interval:
                    return False
            return True
        
        #arithmetic solution to how many subsequences exist in a valid arithmetic sequence
        def numSlices(start:int,end:int):
            length = end-start+1
            num = 0
            if length < 3:
                return num
            for slice_size in range(3,length+1):
                num += length-slice_size+1 # number of slices of that size in this segment
            return num
        
        if size <= 2:
            return ans
        
        interval = A[1]-A[0]
        slice_start = 0
        slice_end = 0
        
        for index in range(1,size):
            this_interval = A[index] - A[index-1]
            if this_interval == interval:
                slice_end = index
            else:
                #print("check",slice_start,"to",slice_end,"with interval",interval)
                ans += numSlices(slice_start,slice_end)
                slice_start = index - 1
                slice_end = index
                interval = this_interval
            if index+1 == size:
                ans += numSlices(slice_start,slice_end)
        return ans

"""
My Solution:
Runtime: 36 ms, faster than 84.89% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 13.3 MB, less than 6.35% of Python3 online submissions for Arithmetic Slices.
"""

"""
Fastest Solution (32ms):
class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        if len(A)<3:
            return 0
        d=A[1]-A[0]
        count=1
        res=0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==d:
                count+=1
            else:
                d=A[i]-A[i-1]
                res+=count*(count-1)//2
                count=1
        if count>1:
            res+=count*(count-1)//2
        return res

Smallest Memory (12380 kb):
class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        res = 0
        l = 0
        while len(A)-l >2:
            diff = A[l+1] - A[l]
            i = l+1
            while i<len(A) and A[i]-A[i-1] == diff:
                if i-l+1 > 2:
                    res+= i - l - 1
                i+=1
                # print(A[l:i+1], i - l - 1, l, i)
            l = i - 1
            
        return res
"""

