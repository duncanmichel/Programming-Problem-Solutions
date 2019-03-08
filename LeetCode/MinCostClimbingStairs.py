"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can 
either start from the step with index 0, or the step with index 1.
Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

#only 256/276 test cases passed
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def pickStep(i):
            size = len(cost)
            [pathThree,pathFour] = [cost[i+2]]*2
            [pathOne,pathTwo] = [cost[i+1]]*2
            if i+3 < size:
                pathOne += cost[i+3]
                pathTwo += cost[i+3]
                pathThree += cost[i+3]
            if i+4 < size:
                pathTwo += cost[i+4]
                pathFour += cost[i+4]
            stepOne = min(pathOne,pathTwo)
            stepTwo = min(pathFour,pathThree)
            if stepOne < stepTwo:
                return i+1
            else:
                return i+2
        
        index = -1
        cheapest = 0
        while index < len(cost)-2:
            index = pickStep(index)
            cheapest += cost[index]
        return cheapest

"""
My Solution

"""

"""
Fastest Solution

"""
