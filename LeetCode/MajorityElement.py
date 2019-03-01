"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxct = 0
        ans = 0
        for n in set(nums):
            ct = nums.count(n)
            if ct > maxct:
                maxct = ct
                ans = n
        return ans

"""
My Solution
Runtime: 48 ms, faster than 86.33% of Python3 online submissions for Majority Element.
Memory Usage: 14.4 MB, less than 5.18% of Python3 online submissions for Majority Element.
"""

"""
Fastest Solution
class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

Smallest Memory:
class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        counter = collections.Counter()
        len_nums = len(nums)
        bar = len_nums // 2
        for num in nums:
            counter[num] += 1
            if counter[num] > bar:
                return num
"""
