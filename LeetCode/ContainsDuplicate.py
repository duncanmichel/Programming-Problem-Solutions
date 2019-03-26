"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true
Example 2:
Input: [1,2,3,4]
Output: false
Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

#using dict to count
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num in counts.keys():
            if counts[num] > 1:
                return True
        
        return False

"""
My Solution:
Runtime: 60 ms, faster than 26.29% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.2 MB, less than 5.05% of Python3 online submissions for Contains Duplicate.
"""

#using set to compare membership [best runtime out of my solutions]
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        for num in nums:
            if num in numset:
                numset.remove(num)
            else:
                return True
        
        return False

"""
My Solution:
Runtime: 52 ms, faster than 42.71% of Python3 online submissions for Contains Duplicate.
Memory Usage: 18.9 MB, less than 24.93% of Python3 online submissions for Contains Duplicate.
"""

#using collections.Counter, actually kind of slow
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numcount = Counter(num for num in nums)
        for i in numcount:
            if numcount[i] > 1:
                return True
        return False

"""
My Solution:
Runtime: 56 ms, faster than 32.02% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.1 MB, less than 5.05% of Python3 online submissions for Contains Duplicate.
"""

"""
Fastest Solution(36ms):
from collections import Counter
class Solution:
    # brute force
#     def containsDuplicate(self, nums: 'List[int]') -> 'bool':
#         if not nums: return False
        
#         temp = []
#         for n in nums:
#             if n not in temp: temp.append(n)
#             else: return True
        
#         return False
    
    # Counter
#     def containsDuplicate(self, nums):
#         if not nums: return False
        
#         c = Counter(nums)
#         for key in c:
#             if c[key] > 1: return True
#         return False

    # Sort
#     def containsDuplicate(self, nums):
#         if not nums: return False
        
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]: return True
#         return False

    # Set
    def containsDuplicate(self, nums):
        if not nums: return False
        return len(nums) != len(set(nums))

Smallest Memory (15144 kb):
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
"""
