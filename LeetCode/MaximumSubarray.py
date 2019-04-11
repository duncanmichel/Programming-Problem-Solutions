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

#Finally working, but really slow. Slightly greedy optimization 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #best = float('-inf')
        best,size = nums[0],len(nums)
        
        if size == 1:
            return best
        
        #base = {i:0 for i in range(size)}
        #memo = dict(base)
        memo = {i:0 for i in range(size)}
        
        memo[0] = best
        for endIndex in range(1,size):
            memo[endIndex] = memo[endIndex-1]+nums[endIndex]
            best = max(best,memo[endIndex])
                
        for firstIndex in range(1,size):
            if nums[firstIndex] > memo[firstIndex]:
                memo[firstIndex] = nums[firstIndex]
                for endIndex in range(firstIndex+1,size):
                    memo[endIndex] = memo[endIndex-1]+nums[endIndex]
                    best = max(best,memo[endIndex])
                best = max(best,memo[firstIndex])
        
        return best

"""
My Solution
Runtime: 600 ms, faster than 5.05% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
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
Fastest Solution (36ms) [O(N)]:
class Solution(object):
    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        maxSum = -inf
        i = j = 0 # sliding window
        numsLen = len(nums)
        while i < numsLen:
            currentSum = 0
            while j < numsLen:
                currentSum += nums[j]
                if currentSum > maxSum:
                    maxSum = currentSum
                if currentSum<0:
                    j+=1
                    break
                j += 1
            i = j
        return maxSum

Alt Fastest Solution (44ms):
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        currSum = largestSum = nums[0]
        for x in nums[1:]:
            currSum = max(x, currSum + x)
            largestSum = max(largestSum, currSum)
        return largestSum

Alt Fastest Solution (52ms) [DP Solution]:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        R = [0 for _ in range(n)]
        
        R[0] = max(0, nums[0])
        maxSum = nums[0]
        
        for i in range(1, n):
            R[i] = max(R[i-1] + nums[i], nums[i])
            maxSum = max(maxSum, R[i])
        
        return maxSum

Smallest Memory (12508 kb):
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        leftIndex = rightIndex = 0
        tmpMax = finalMax = nums[0]
        for i in range(1, len(nums)):
            if (tmpMax<0):
                leftIndex = rightIndex = i
                tmpMax = nums[i]
            else:
                tmpMax += nums[i]
            if (finalMax < tmpMax):
                finalMax = tmpMax
                rightIndex = i
        return finalMax
"""
