"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]
Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

#arithmetic solution, runs in linear time and near constant space (only enough memory to hold variables
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        numsum = 0
        totalsum = 0
        for index in range(size):
            numsum += nums[index]
            totalsum += index
        totalsum += size
        return totalsum - numsum
"""
My Solution:
Runtime: 48 ms, faster than 68.08% of Python3 online submissions for Missing Number.
Memory Usage: 14.1 MB, less than 5.25% of Python3 online submissions for Missing Number.
"""

#using set, greater than constant space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(nums)
        index = 0
        for num in numset:
            if num != index:
                return index
            index += 1
        return index
"""
My Solution:
Runtime: 60 ms, faster than 34.64% of Python3 online submissions for Missing Number.
Memory Usage: 14.5 MB, less than 5.25% of Python3 online submissions for Missing Number.
"""

#by sorting list first, still less then linear runtime and more than constant space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mynums = sorted(nums)
        size = len(nums)
        for index in range(size):
            if mynums[index] != index:
                return index
        return size
"""
My Solution:
Runtime: 68 ms, faster than 21.17% of Python3 online submissions for Missing Number.
Memory Usage: 14.2 MB, less than 5.25% of Python3 online submissions for Missing Number.
"""

"""
Fastest Solution (36ms):
class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        return  sum(range(len(nums)+1)) - sum(nums)

Smallest Memory (13040 kb):
class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res = res^len(nums)
        return res
"""
