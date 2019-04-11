"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def checkSides(leftNode,rightNode):
            if leftNode is None and rightNode is None:
                return True
            elif leftNode is None or rightNode is None:
                return False
            elif leftNode.val != rightNode.val:
                return False
            else:
                return checkSides(leftNode.right,rightNode.left) and checkSides(leftNode.left,rightNode.right)
        
        return checkSides(root.left,root.right)

"""
My Solution:
Runtime: 40 ms, faster than 98.97% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.3 MB, less than 5.61% of Python3 online submissions for Symmetric Tree.
"""

"""
Fastest Solution (36ms) [iterative solution]:
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (root.left == None and root.right == None):
            return True
        chk = []
        if root.left and root.right:
            chk = [root.left,root.right]
        else:
            return False
        
        while chk:
            l = chk.pop(0)
            r = chk.pop(0)
            
            if l.val != r.val:
                return False
            
            if l.left and r.right:
                chk.append(l.left)
                chk.append(r.right)
            
            elif l.left or r.right:
                return False
            
            if l.right and r.left:
                chk.append(l.right)
                chk.append(r.left)
            
            elif l.right or r.left:
                return False
        return True


Smallest Memory (12248 kb):
class Solution:
    def compare(self, lleft, rright):
        if (not lleft) and (not rright):
            return True
        elif (not lleft) or (not rright):
            return False
        else:
            if lleft.val != rright.val:
                return False
            else:
                return self.compare(lleft.left, rright.right) and self.compare(lleft.right, rright.left)
    
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        #recursive
        if not root:
            return True
        else:
            return self.compare(root.left, root.right)
"""
