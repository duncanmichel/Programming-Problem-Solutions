"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only 
constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can 
rob tonight without alerting the police.
Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #working recursive solution, but too long
        def remainingHouses(index,loot):
            if index == size:
                return 0 + loot
            elif index == size-1:
                return nums[index] + loot
            return max(remainingHouses(index+2,loot + nums[index]),remainingHouses(index+1,loot))
        
        size,loot,memo = len(nums),0,{-2:0,-1:0}
        for index in range(size):
            if index-2 in memo:
                memo[index] = max(memo[index-2]+nums[index],memo[index-1])
            else:
                memo[index] = nums[index]
            loot = max(loot,memo[index])

        return loot

"""
My Solution:
Runtime: 32 ms, faster than 11.32% of Python online submissions for House Robber.
Memory Usage: 11.7 MB, less than 5.29% of Python online submissions for House Robber.
"""

"""
Fastest Solution ():


Smallest Memory ():

"""
