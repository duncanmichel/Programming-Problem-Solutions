"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My Recursive Solution (divide the sorted array in half recursively)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(firstIndex,endIndex) -> TreeNode:
            if firstIndex > endIndex:
                return None
            elif firstIndex == endIndex:
                return TreeNode(nums[firstIndex])
            
            breadth = endIndex - firstIndex
            if breadth == 1:
                thisTree = TreeNode(nums[endIndex])
                thisTree.left = TreeNode(nums[firstIndex])
            else:
                midpoint = firstIndex + int(breadth/2)
                thisTree = TreeNode(nums[midpoint])
                thisTree.left = buildTree(firstIndex,midpoint-1)
                thisTree.right = buildTree(midpoint+1,endIndex)
            return thisTree
        
        def traverseTree(tree:TreeNode):
            if tree == None:
                return None
            print (tree.val)
            traverseTree(tree.left)
            traverseTree(tree.right)
        
        size = len(nums)
        if size == 0:
            return None
        elif size == 1:
            bst = TreeNode(nums[0])
            return bst
        else:
            middle = int(size/2)
            bst = TreeNode(nums[middle])
        
        bst.left = buildTree(0,middle-1)
        bst.right = buildTree(middle+1,size-1)
        
        #traverseTree(bst)
        
        return bst

"""
My Solution:
Runtime: 64 ms, faster than 82.01% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 5.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""

"""
Fastest Solution (56ms):
class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None
        
        return self.toBstUtil(nums, 0, len(nums) - 1)
    
    def toBstUtil(self, nums, low, high):
        
        if low > high:
            return None
        
        mid = (low + high) // 2
        
        node = TreeNode(nums[mid])       
        node.left = self.toBstUtil(nums, low, mid - 1)
        node.right = self.toBstUtil(nums, mid + 1, high)
        
        return node

Smallest Memory (14528 kb):
class Solution:
    def helper(self, num, first, last):
        if last < first:
            return None

        mid = first+(last-first) // 2

        root = TreeNode(num[mid])
        root.left = self.helper(num, first, mid-1)
        root.right = self.helper(num, mid+1, last )

        return root
    
    def sortedArrayToBST(self, num):
        return self.helper(num, 0, len(num)-1)
"""
