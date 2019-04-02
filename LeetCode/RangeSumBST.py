"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Recursive
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        elif L > root.val or R < root.val:
            return 0 + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
        else:
            return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
"""
My Solution:
Runtime: 312 ms, faster than 24.22% of Python3 online submissions for Range Sum of BST.
Memory Usage: 21.7 MB, less than 5.06% of Python3 online submissions for Range Sum of BST.
"""

#Iterative (but using a list for a stack); slightly faster
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        sum = 0
        if root == None:
            return sum
        while stack != [] or root != None:
            if root == None:
                #print("root is none")
                root = stack.pop()
            elif L > root.val or root.val > R:
                #print('val not in range',root.val)
                stack.append(root.right)
                root = root.left
            else:
                sum += root.val
                #print("sum now",sum,"val",root.val)
                stack.append(root.right)
                root = root.left   
        return sum
"""
My Solution:
Runtime: 304 ms, faster than 27.75% of Python3 online submissions for Range Sum of BST.
Memory Usage: 21.8 MB, less than 5.06% of Python3 online submissions for Range Sum of BST.
"""

#slight optimization, based on iterative interpretation of "fastest solution" 
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        sum = 0
        if root == None:
            return sum
        while stack != [] or root != None:
            if root == None:
                #print("root is none")
                root = stack.pop()
                continue
            if L <= root.val <= R:
                sum += root.val
                #print("sum now",sum,"val",root.val)
            else:
                #print("val out of range",root.val)
                root = root
            if root.val < R and root.right:
                stack.append(root.right)
            if L < root.val and root.left:
                stack.append(root.left)
            if stack != []:
                root = stack.pop()
            else:
                break
        return sum
"""
My Solution:
Runtime: 256 ms, faster than 55.49% of Python3 online submissions for Range Sum of BST.
Memory Usage: 21.9 MB, less than 5.06% of Python3 online submissions for Range Sum of BST.
"""

"""
Fastest Solution (204ms):
class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        self.sum = 0
        
        def traverseBST(treeNode):
            if treeNode.val >= L and treeNode.val <=R:
                self.sum += treeNode.val
            if treeNode.val > L and treeNode.left:
                traverseBST(treeNode.left)
            if treeNode.val < R and treeNode.right:
                traverseBST(treeNode.right)  
            
        traverseBST(root)
        return self.sum

Smallest Memory (20664 kb):
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
"""
