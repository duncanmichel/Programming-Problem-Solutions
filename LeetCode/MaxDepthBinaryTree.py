

"""
Problem Description
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #print("[DEBUG] current node: " + str(root.val))
        if root == None:
            return 0
        elif (root.left == None) and (root.right == None):
            return 1
        elif root.left == None:
            #print("[DEBUG] Checking depth of: " + str(root.right.val))
            return 1 + self.maxDepth(root.right)
        elif root.right == None:
            #print("[DEBUG] Checking depth of: " + str(root.left.val))
            return 1 + self.maxDepth(root.left)
        else:
            #print("[DEBUG] Checking depth of: " + str(root.left.val) + " and " + str(root.right.val))
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

"""
Fastest Solution:
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        from collections import deque
        queue =deque()
        queue.append(root)
        layer = 0
        while queue:
            new_queue = deque()
            while queue:
                cur = queue.popleft()
                if cur.left:
                    new_queue.append(cur.left)
                if cur.right:
                    new_queue.append(cur.right)
            queue = new_queue
            layer += 1
        return layer
"""
