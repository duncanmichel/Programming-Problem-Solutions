"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf 
to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        def traverse(node,level):
            if node is None:
                return None
            #print("node:",node.val,"level:",level,"cur state of levels:",levels)
            if level + 1 > len(levels):
                levels.append([node.val])
                traverse(node.left,level+1)
                traverse(node.right,level+1)
            else:
                traverse(node.left,level+1)
                traverse(node.right,level+1)
                levels[level].append(node.val)
            return None
            
        if root is None:
            return levels
        traverse(root,0)
        return levels[::-1]
        
"""
My Solution:
Runtime: 44 ms, faster than 78.34% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.2 MB, less than 5.23% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""

"""
Fastest Solution (36ms):
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        
        result, current = [], [root]
        while current:
            next_level, values = [], []
            for node in current:
                values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            current = next_level
            result.append(values)
        return result[::-1]  

Smallest Memory (12468 kb):
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        if root:
            q = [root]
            while q :
                res.append([node.val for node in q])
                new_q = []
                for node in q:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                q = new_q
        res2 = []
        while res:
            temp = res.pop()
            res2.append(temp)
"""
