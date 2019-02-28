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



"""
My Solution:

"""

"""
Fastest Solution:

"""
