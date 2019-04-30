"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it 
reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 
nodes before the intersected node in B.
Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it 
reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node 
before the intersected node in B.
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect,
intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        if headA == headB:
            return headA
        
        diffA = 0
        diffB = 0
        pointA = headA
        pointB = headB
        while pointA and pointB:
            pointA,pointB = pointA.next,pointB.next
        while pointA:
            pointA = pointA.next
            diffA += 1
        while pointB:
            pointB = pointB.next
            diffB += 1
        while diffA:
            headA = headA.next
            diffA -= 1
        while diffB:
            headB = headB.next
            diffB -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA,headB = headA.next,headB.next
        return None
            

"""
My Solution:
Runtime: 208 ms, faster than 72.94% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.7 MB, less than 5.17% of Python online submissions for Intersection of Two Linked Lists.
"""

"""
Fastest Solution (184ms):
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        la = self.length(headA)
        lb = self.length(headB)
        curA = headA
        curB = headB
        while(la>lb):
            curA = curA.next
            la -= 1
        while(lb>la):
            curB = curB.next
            lb -= 1
        while(curA!=curB):
            curA = curA.next
            curB = curB.next
        return curA
    def length(self,head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l

Smallest Memory (40588 kb):
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB
        
        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            
            if pB is None:
                pB = headA
            else:
                pB = pB.next
    
        return pA
"""
