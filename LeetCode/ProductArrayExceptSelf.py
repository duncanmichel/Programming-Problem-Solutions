"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements 
of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity 
analysis.)
"""

"""
Draft Solution (too slow):
from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod (l,r):
            return reduce((lambda a,b: a*b),nums[l:r])
        
        if nums is None:
            return 0
        
        ans = nums.copy()
        
        for i in range(0,len(nums)):
            if i == 0:
                ans[i] = prod(i+1,len(nums))
            elif i == len(nums)-1:
                ans[i] = prod(0,i)
            else:
                ans[i] = prod(0,i) * prod(i+1,len(nums))
        return ans
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return 0
        
        temp = 1
        ans = []
        
        #first time going through the array, it's beginning to the end. p keeps a running total of the product, and each element will equal the running total of the products of the elements
        for i in range (0,len(nums)): #
            ans.append(temp)
            temp *= nums[i]
        
        temp = 1
        
        #the 2nd time going through the array, you're doing the same process, but backwards, finishing off the result by multiplying the elements that came after.
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= temp
            temp *= nums[i]
        
        return ans


"""
My Solution:
Runtime: 120 ms, faster than 32.48% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.8 MB, less than 5.12% of Python3 online submissions for Product of Array Except Self.
"""

"""
Fastest Solution:
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
"""
