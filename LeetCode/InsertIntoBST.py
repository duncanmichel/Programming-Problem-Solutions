"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the 
root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any 
of them.
For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
"""

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
            return root
        else:
            root.right = self.insertIntoBST(root.right,val)
            return root

"""
My Solution:
Runtime: 124 ms, faster than 66.38% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16.2 MB, less than 8.00% of Python3 online submissions for Insert into a Binary Search Tree.
"""

"""
Fastest Solution (100ms):
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            if not root.left:
                node = TreeNode(val)
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root

Smallest Memory (15252 kb):
class Solution:
    def insertIntoBST(self, root, val):
        if(root == None): return TreeNode(val);
        if(root.val < val): root.right = self.insertIntoBST(root.right, val);
        else: root.left = self.insertIntoBST(root.left, val);
        return(root)
"""
