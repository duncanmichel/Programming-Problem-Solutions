"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

#Added hash function for the lists and memoization to eliminate redundant computation of permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        memo = {}
        def hashList(numList):
            count = 0
            tens = 1
            for num in reversed(numList):
                count += num * tens
                tens *= 10
            return count
        
        def recursPermute (numList):
            size = len(numList)
            if size <= 1:
                return [numList]
            listHash = hashList(numList)
            if listHash in memo:
                return memo[listHash]
            ans = []
            for index in range(size):
                for newList in self.permute(numList[0:index]+numList[index+1:size]):
                    #print("list",newList,"is list:",type(newList) is list)
                    ans.append([numList[index]]+newList if type(newList) is list else [numList[index],newList])
            memo[listHash] = ans
            return ans
        
        return recursPermute(nums)
        
"""
My Solution:
Runtime: 56 ms, faster than 35.12% of Python3 online submissions for Permutations.
Memory Usage: 13.2 MB, less than 5.23% of Python3 online submissions for Permutations.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size <= 1:
            return [nums]
        ans = []
        for index in range(size):
            for newList in self.permute(nums[0:index]+nums[index+1:size]):
                #print("list",newList,"is list:",type(newList) is list)
                ans.append([nums[index]]+newList if type(newList) is list else [nums[index],newList])
        return ans

"""
My Solution:
Runtime: 72 ms, faster than 6.25% of Python3 online submissions for Permutations.
Memory Usage: 13.1 MB, less than 5.23% of Python3 online submissions for Permutations.
"""

"""
Fastest Solution (44ms):
class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

Smallest Memory (12260 kb):
class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        #T(n) = O(n) + T(n-1)
        '''
        out = []
        temp = []
        def helper(nums, temp, out):
            
            if not nums:
                out.append(temp)
                return

            for i in range(len(nums)):
                new_temp = temp + [nums[i]]
                new_nums = nums[:i] + nums[i+1:]
                helper(new_nums, new_temp, out)
               
        helper(nums, temp, out)
        return out
"""
