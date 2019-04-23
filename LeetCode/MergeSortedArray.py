"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2index = 0
        nums2append = 0
        temp = nums1[0]
        temp2 = 0
        for index in range(len(nums1)):
            #print("index",index,"num1 val",nums1[index],"num2 index",nums2index,"num2 val",nums2[nums2index])
            if n == 0:
                break
            if m+n > index >= m:
                nums1[index] = nums2[nums2index]
                nums2index += 1
            elif nums1[index] > nums2[nums2index]:
                temp = nums1[index]
                nums1[index] = nums2[nums2index]
                nums2append = nums2index + 1
                while nums2append < len(nums2): #insert value into nums2
                    if temp < nums2[nums2append]:
                        temp2 = nums2[nums2append]
                        nums2[nums2append] = temp
                        temp = temp2
                    nums2append += 1
                nums2.append(temp)
                nums2index += 1
            
            elif index >= m+n:
                break

"""
My Solution:
Runtime: 48 ms, faster than 22.33% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.2 MB, less than 5.09% of Python3 online submissions for Merge Sorted Array.
"""

#Cheating a bit, but works
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
'''
Runtime: 52 ms, faster than 18.96% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Merge Sorted Array.
'''

"""
Fastest Solution (32ms):
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        '''
        Do not return anything, modify nums1 in-place instead.
        '''
        
        new_arr_ptr = 0
        mmin = min(m,n)
        ptr_1 = 0
        ptr_2 = 0
        
        while ptr_1 < m and ptr_2 < n:
            if nums1[m-1-ptr_1] > nums2[n-1-ptr_2]:
                nums1[m+n-1-new_arr_ptr] = nums1[m-1-ptr_1]
                ptr_1 += 1
            else:
                nums1[m+n-1-new_arr_ptr] = nums2[n-1-ptr_2]
                ptr_2 += 1                
            new_arr_ptr += 1
            
        while ptr_1 < m:
            nums1[m+n-1-new_arr_ptr] = nums1[m-1-ptr_1]
            ptr_1 += 1
            new_arr_ptr += 1
        while ptr_2 < n:
            nums1[m+n-1-new_arr_ptr] = nums2[n-1-ptr_2]
            ptr_2 += 1
            new_arr_ptr += 1

Alt Fastest (36ms):
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2:
            return
        while n:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n = n -1

Smallest Memory (12128 kb):
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        nums1[:] = sorted(nums1[:m]+nums2)
"""
