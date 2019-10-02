"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false
Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numMap = {x:0 for x in set(arr)}
        for num in arr:
            numMap[num] += 1        
        return len(numMap) == len(set(numMap.values()))

"""
My Solution:
Runtime: 44 ms, faster than 63.25% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
"""


"""
Fastest Solution (32ms):
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:   
        count_dict = defaultdict(int)
        for a in arr:
            count_dict[a] += 1  
        if len(count_dict) == len(set(count_dict.values())):
            return True
        else:
            return False

Alt Fastest (40ms):
import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(collections.Counter(arr).values())) == len(collections.Counter(arr))
        
Smallest Memory ():
Not enough solutions
"""
