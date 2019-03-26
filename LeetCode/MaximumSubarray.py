"""

"""

# only 200 of 202 test cases - O[N^2] solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        if len(nums) == 1:
            return nums[0]
        elif nums == []:
            return 0
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)+1):
                best = max(best,sum(nums[x:y]))
        return best

# O[2N] - essentially O[N} solution in two passes, one to add all, one to subtract all (passes 196/202 cases)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]

        base = nums[0]
        maxNum = nums[0]
        stopIndex = len(nums)
        baseFinalIndex = 0
        for x in range(1,len(nums)):
            if base + nums[x] > base: #positive number
                baseFinalIndex = x
            base += nums[x]
            maxNum = max(maxNum,nums[x])
            if base > best:
                best = base
                stopIndex = x
            print("going up at index",x,"base",base,"best",best,"stop at",stopIndex)
        copy = best
        for y in range(0,stopIndex):
            base -= nums[y]
            copy -= nums[y]
            best = max(base,best,copy)
            print("going down at index",y,"base",base,"copy",copy,"best",best)
        for y in range(stopIndex,min(len(nums)-1,baseFinalIndex)):
            base -= nums[y]
            best = max(base,best)
            print("going down at index",y,"base",base,"best",best)
        if maxNum > best:
            best = maxNum
        return best

"""
My Solution

"""

"""
Fastest Solution


Smallest Memory

"""
