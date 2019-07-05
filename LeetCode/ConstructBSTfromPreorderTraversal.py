"""
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any 
descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then 
traverses node.left, then traverses node.right.)
Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        size = len(preorder)
        def helper(index,middle):
            if index >= size: return None,index
            root = TreeNode(preorder[index])
            middle = root.val if root.val > middle else middle
            index += 1
            if index >= size: return root,index
            if preorder[index] < root.val:
                root.left,index = helper(index,root.val)
            if index >= size: return root,index
            if preorder[index] > root.val and (root.val == middle or preorder[index] < middle):
                root.right,index = helper(index,middle)
            return root,index
            
        tree,index = helper(0,preorder[0])
        return tree

"""
My Solution:
Runtime: 40 ms, faster than 76.02% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 13.4 MB, less than 5.15% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
"""


"""
Fastest Solution (24ms):
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        n = len(preorder)
        index = 1
        for i in range(1, n):
            if preorder[i] < preorder[0]:
                index = i + 1
        
        root.left = self.bstFromPreorder(preorder[1: index])
        root.right = self.bstFromPreorder(preorder[index:])
        return root
        
Smallest Memory (12744 kb):
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        parent = preorder[0]
        for i in range(1,len(preorder)):
            if preorder[i] < stack[-1].val:
                stack.append(TreeNode(preorder[i]))
                stack[-2].left = stack[-1]
                
            else:
                if len(stack) > 1:
                    while(len(stack)>1):
                        if (preorder[i]>stack[-2].val):
                            stack.pop()
                        else:
                            stack.append(TreeNode(preorder[i]))
                            temp = stack[-2]
                            while temp.right:
                                temp = temp.right
                            temp.right = stack[-1]
                            break    
                if len(stack) == 1:
                    temp = stack.pop()
                    temp.right = TreeNode(preorder[i])
                    stack.append(temp.right)                
        return root 
"""
