"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        
        def halfSum(start,remainder):
            for index in range(start,size):
                if nums[index] == remainder:
                    return index
            return -1
        
        for numIndex in range(size):
            #if nums[numIndex] <= target: #this might work
            temp = halfSum(numIndex+1,target-nums[numIndex])
            if temp >= 0:
                return [numIndex,temp]
        return [-1,-1]

"""
My Solution:
Runtime: 3172 ms, faster than 28.88% of Python3 online submissions for Two Sum.
Memory Usage: 13.6 MB, less than 46.90% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        for num in nums:
            for i in range(count+1,len(nums)):
                if num + nums[i] == target:
                    return [count,i]
            count += 1
        return [0,0]
    
"""
My Solution:
Runtime: 4412 ms, faster than 19.82% of Python3 online submissions for Two Sum.
Memory Usage: 13.8 MB, less than 25.44% of Python3 online submissions for Two Sum.
"""

"""
Fastest Solution:
class Solution:
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            dic[target-num] = i

Most Common Fast Solution:
class Solution:
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
 
        hashmap={}
        for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num]=index
        return None
"""
