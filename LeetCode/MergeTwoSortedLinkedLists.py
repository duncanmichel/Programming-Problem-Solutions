"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Short circuit the initial checks in the first loop condition:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = l1, l2
        head = None
        pointer = head
        
        while list1 and list2:
            if pointer:
                pointer.next = list1 if list1.val < list2.val else list2
                pointer = pointer.next
            else:
                head = list1 if list1.val < list2.val else list2
                pointer = head
            list1 = list1.next if pointer == list1 else list1
            list2 = list2.next if pointer == list2 else list2
        
        if head:
            pointer.next = list1 if list1 else list2
        else:
            return list1 if list1 else list2
        
        return head

"""
My Solution:
Runtime: 44 ms, faster than 86.91% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.1 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
"""

#Slow...
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = l1, l2
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        pointer = head
        
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        
        if list1 is None:
            pointer.next = list2
        else:
            pointer.next = list1
        
        return head

"""
My Solution:
Runtime: 56 ms, faster than 18.59% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.3 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
"""

"""
Fastest Solution (36ms):
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if(l1 is None):
            return l2
        elif(l2 is None):
            return l1
        else:
            
            if(l1.val<l2.val):
                newlist = l1
                l1=l1.next
            else:
                newlist = l2
                l2=l2.next
            h = newlist
            while(l1 and l2):
                if(l1.val<l2.val):
                    h.next = l1
                    h = h.next
                    l1=l1.next
                else:
                    h.next=l2
                    h = h.next
                    l2=l2.next
                
            while(l1):
                h.next = l1
                l1 = l1.next
                h = h.next
            while(l2):
                h.next = l2
                l2 = l2.next
                h = h.next
        return newlist

Smallest Memory (12144 kb):
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        l_ret = None
        n = l_ret
        
        while l1 or l2:
            if not l2 or (l1 is not None and l1.val <= l2.val):
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            
            if l_ret is None:
                l_ret = ListNode(val)
                n = l_ret
            else:
                n.next = ListNode(val)
                n = n.next
"""
