"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def rotate(self, nums, k):
        size = len(nums)
        rotateIndex = k % size
        
        temp = nums[size-rotateIndex:size]
        
        nums[rotateIndex:] = nums[:size-rotateIndex]
        
        nums[:rotateIndex] = temp

"""
My Solution:
Runtime: 48 ms, faster than 62.85% of Python online submissions for Rotate Array.
Memory Usage: 11.9 MB, less than 5.01% of Python online submissions for Rotate Array.
"""

"""
Fastest Solution (36ms):
class Solution(object):
    def rotate(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        '''
        n = len(nums)
        k = k % len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]

Alt Fastest (40ms) [I like this algorithmic approach):
class Solution(object):
    def rotate(self, nums, k):
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        k = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

Smallest Memory (11184 kb):
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
    
    
    # 反转nums[m, n] 
    def reverse(self, nums, m, n):
        i, j = m, n
        while i < j:
            self.swap(nums, i, j) 
            i += 1
            j -= 1
            

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
"""
