"""
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1 = len(nums1)
        size2 = len(nums2)
        ans = []
        
        if size1 == 0 or size2 == 0:
            return ans
        
        nums1.sort()
        nums2.sort()
        
        if size1 >= size2:
            greater = nums1
            lesser = nums2
        else:
            greater = nums2
            lesser = nums1
            
        index = 0
        gsize = len(greater)

        for num in lesser:
            if index == gsize:
                break
            while index < gsize and num > greater[index]:
                index += 1
            if index < gsize and num == greater[index]:
                ans += [num]
                index += 1
            
        return ans

"""
My Solution:
Runtime: 40 ms, faster than 88.05% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.2 MB, less than 5.81% of Python3 online submissions for Intersection of Two Arrays II.
"""

"""
Fastest Solution (32ms):
class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        # first the dict will have the numbers and number of occurence 
        # then whenever we find a number in list2 which is in dict we remove that from the dict
        # when all entry removed then no more common
        # and pic that number for result array
        d = {}
        result = []
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in nums2:
            if (j in d) and ( 0 != d[j]):
                result.append(j)
                d[j] -= 1
                
        return (result)

Smallest Memory (12208 kb):
class Solution:
    def intersect(self, nums1, nums2):
        idx, result, len1, len2 = 0, [], len(nums1), len(nums2)
        if len1 < len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        nums1.sort()
        while idx < len2 and nums1:
            low, high = 0, len1 - 1
            while low <= high:
                mid = (low + high)//2
                if nums1[mid] == nums2[idx]:
                    result.append(nums1.pop(mid))
                    len1 -= 1
                    break
                elif nums1[mid] > nums2[idx]:
                    high = mid - 1
                else:
                    low = mid + 1
            idx += 1
        return result
"""
