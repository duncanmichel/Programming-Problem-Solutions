"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in 
T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            gval,lval = p.val,q.val
        else:
            gval,lval = q.val,p.val
        def find(node):
            if node is None: return None
            if node == p or node == q: return node
            nval = node.val
            if lval < nval < gval: return node
            elif gval < nval: return find(node.left)
            return find(node.right) #nval < lval
        return find(root)
        
#same runtime, but shouldn't, since doesn't take full advantage of BST structure
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if node is None: return None
            if node == p or node == q: return node
            left,right = find(node.left),find(node.right)
            if left is None: return right
            return left if right is None else node
        return find(root) 

"""
My Solution:
Runtime: 84 ms, faster than 89.38% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 17.4 MB, less than 5.18% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""

#original solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def hasDescendant(node):
            if node is None:
                return False
            print("Searching for p and q at Node",node.val)
            if node == p or node == q:
                return True
            return hasDescendant(node.left) or hasDescendant(node.right)
            
        def ancestor(node):
            if node is None:
                return None
            print("checking ancestry of Node",node.val)
            left = hasDescendant(node.left)
            right = hasDescendant(node.right)
            if left and right:
                return node
            elif node == p or node == q and (left or right):
                return node
            elif left:
                return ancestor(node.left)
            return ancestor(node.right)
            
        return ancestor(root)

"""
My Solution:
Runtime: 116 ms, faster than 6.45% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 17.5 MB, less than 5.18% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""

"""
Fastest Solution (76ms):
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root is None:
                return
            
            if root.val == p.val or root.val ==q.val:
                return root
            
            if ((p.val < root.val < q.val) or (q.val < root.val < p.val)):
                return root
            
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
            
        return dfs(root, p, q)

Smallest Memory (16496 kb): #not sure how this works
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root
"""
