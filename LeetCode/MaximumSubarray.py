"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its 
sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
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

#Another take on two-step pass (forward and backward), but only passes 182/202 test cases
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        ans,size = nums[0],len(nums)
        
        if size == 1:
            return ans
        
        bestForward,bestBackward = nums[0],nums[-1]
        maxNum = max(best,bestForward)
        forwardIndex,backwardIndex,count = 0,size-1,1
        #print("[forward-start] total",maxNum,"best forward",bestForward,"at index",forwardIndex,"starting index",count)
        for num in nums[1:]:  
            maxNum += num
            if maxNum >= bestForward:
                bestForward = maxNum
                forwardIndex = count
            #print("[forward] total",maxNum,"best forward",bestForward,"at index",forwardIndex,"current index",count,"cur char",num)
            count +=1
                
        maxNum = max(best,bestBackward)
        count = size-2
        #print("[backward-start] total",maxNum,"best backward",bestBackward,"at index",backwardIndex,"starting index",count)
        for num in nums[size-2::-1]:
            maxNum += num
            if maxNum >= bestBackward:
                bestBackward = maxNum
                backwardIndex = count
            #print("[backward] total",maxNum,"best backward",bestBackward,"at index",backwardIndex,"current index",count,"cur char",num)
            count -=1
        
        ans = 0
        if backwardIndex > forwardIndex:
            ans = max(nums)
        for index in range(backwardIndex,forwardIndex+1):
            ans += nums[index]
        
        #print("[final] total",maxNum,"best forward",bestForward,"at index",forwardIndex,"best backward",bestBackward,"at index",backwardIndex," final answer:",ans)
        
        return ans

"""
My Solution

"""

"""
Fastest Solution


Smallest Memory

"""
