"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Note:
The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
"""

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levelSum = dict()
        def helper(node,level):
            if node is None:
                pass
            else:
                if level not in levelSum:
                    levelSum[level] = 0
                levelSum[level] += node.val
                helper(node.left,level+1)
                helper(node.right,level+1)
        helper(root,1)
        ans = 1
        lSum = 0
        for key in levelSum.keys():
            if levelSum[key] > lSum:
                lSum = levelSum[key]
                ans = key
        return ans

"""
My Solution:
Runtime: 360 ms, faster than 33.23% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
Memory Usage: 18.4 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
"""


"""
Fastest Solution (284ms):
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxSumLvl = (float('-inf'), -1)
        lvl, n = [root], 1
        while any(lvl):
            maxSumLvl = max(maxSumLvl, (sum(n.val for n in lvl), n))
            lvl, n = [c for n in lvl for c in (n.left, n.right) if c], n+1
        return maxSumLvl[1]

Smallest Memory:
[not avail at this time]
"""
