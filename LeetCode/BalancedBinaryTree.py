# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def height(self,root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return ((abs(self.height(root.left) - self.height(root.right))) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
     
    """
    Fastest Solution:
    
        def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if node == None: return 0
            left = depth(node.left)
            if left == -1: return -1
            right = depth(node.right)
            if right == -1: return -1
            if abs(left-right) <= 1:
                return max(left,right)+1
            return -1
        res = depth(root)
        return res != -1
        
    Alternate Fastest:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.helper(root) != -1
        
        
        
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        if left == -1:
            return -1
        right = self.helper(node.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return 1+max(left, right)
    
    """
