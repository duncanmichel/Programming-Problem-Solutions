"""
Given a non-empty array of integers, return the k most frequent elements.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        each = set(nums)
        counts = {}
        ans = []
        for num in each:
            counts[num] = nums.count(num)
        for i in range(0,k):
            curmax = max(counts.values())
            for n in counts:
                if counts[n] == curmax:
                    ans.append(n)
                    counts.pop(n)
                    break
        return ans

"""
My Solution:
Runtime: 1684 ms, faster than 5.24% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 15.9 MB, less than 8.41% of Python3 online submissions for Top K Frequent Elements.
"""

"""
Fastest Solution:
class Solution:
    def topKFrequent(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        '''
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)

Alt Fastest Solution:
class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
"""
