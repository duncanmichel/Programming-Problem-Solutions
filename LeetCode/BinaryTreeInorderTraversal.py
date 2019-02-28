"""
Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Recursive Solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
 
"""
My Solution:
Runtime: 40 ms, faster than 38.89% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.1 MB, less than 5.64% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
 
#Iterative Solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        #if isinstance(root,TreeNode):
            #return ["node"]
        ans = []
        todo = []
        cur = root
        todo = [cur.left,cur.val,cur.right]
        cur = cur.left
        #print("Initial todo: ","".join(list(map(str,todo))))
        while todo:
            cur = todo.pop(0)
            if cur is None:
                continue
            elif isinstance(cur,int):
                ans += [cur]
            else:
                todo = [cur.left,cur.val,cur.right] + todo
                cur = cur.left
                #print("Current todo: ",todo)
        return ans

"""
My Solution:
Runtime: 56 ms, faster than 15.72% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.3 MB, less than 5.64% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
 
"""
Fastest Solution:
class Solution:
    def inorderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: List[int]
        '''
        ans = []
        st = []
        while True:
            while root:
                st.append(root)
                root = root.left
            if not st:
                return ans
            root = st.pop()
            ans.append(root.val)
            root = root.right
"""
