"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
A node is deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is that node, plus the set of all descendants of that node.
Return the node with the largest depth such that it contains all the deepest nodes in its subtree.
Example 1:
Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
Note:
The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepestNode(node:TreeNode,depth:int) -> TreeNode:
            if node is None:
                return (None,depth)
            left,ldepth = deepestNode(node.left,depth+1)
            right,rdepth = deepestNode(node.right,depth+1)
            if ldepth == rdepth:
                return (node,ldepth)
            return (left,ldepth) if ldepth > rdepth else (right,rdepth)
        
        return deepestNode(root,0)[0]

"""
My Solution:
Runtime: 40 ms, faster than 85.96% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
Memory Usage: 13.1 MB, less than 16.67% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
"""

"""
Fastest Solution (32ms):
class Solution:
    def subtreeWithAllDeepest(self, root):
        if not root:
            return []
        def findingMostBalanced(root, depth):
            if not root:
                return None, depth

            left, depth1 = findingMostBalanced(root.left, depth+1)
            right, depth2 = findingMostBalanced(root.right, depth+1)
   
            if depth1 == depth2: return root, depth1
    
            elif depth1 > depth2: return left, depth1
            
            else: return right, depth2
        
        ret, depth = findingMostBalanced(root, 0)
        return ret

Smallest Memory (12508 kb):
class Solution:
    def subtreeWithAllDeepest(self, root: 'TreeNode') -> 'TreeNode':
        
        def get_subtree_with_deepest(node, depth):
            
            if not node.left and not node.right:
                return (node, depth)
            elif not node.left:
                return get_subtree_with_deepest(node.right, depth + 1)
            elif not node.right:
                return get_subtree_with_deepest(node.left, depth + 1)
            
            l_node, l_depth = get_subtree_with_deepest(node.left, depth + 1)
            r_node, r_depth = get_subtree_with_deepest(node.right, depth + 1)
            
            if l_depth > r_depth:
                return (l_node, l_depth)
            elif r_depth > l_depth:
                return (r_node, r_depth)
            else:
                return(node, l_depth)
            
        if not root:
            return root
        
        return get_subtree_with_deepest(root, 0)[0]
"""
