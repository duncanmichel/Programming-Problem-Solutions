"""
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        #else
        preList = self.reverseList(head.next)
        newList = ListNode(head.val)
        #print("[DEBUG] current newList val: "+str(newList.val))
        tempList = preList
        while tempList.next != None:
            tempList = tempList.next
        tempList.next = newList
            
        return preList
        
"""
Fastest Solution:
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        head_new = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = head_new
            head_new = cur
            cur = temp
        return head_new
        
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

Least Memory Used Solution:
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        current = head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        res = []
        while prev:
            res.append(prev.val)
            prev = prev.next
        return res

"""
