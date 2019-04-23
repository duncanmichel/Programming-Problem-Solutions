"""
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

#2 * O[N] time, O[N] space, though
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        stack = [head.val]
        pointer = head.next
        head.next = None
        while pointer is not None:
            stack.append(pointer.val)
            temp = pointer.next
            pointer.next = head
            head = pointer
            pointer = temp
        stack.reverse()
        #print("stack",stack)
        #print("head.val",head.val)
        while head is not None:
            if head.val != stack.pop():
                return False
            head = head.next
        
        return len(stack) == 0

"""
My Solution:
Runtime: 84 ms, faster than 45.72% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23.6 MB, less than 13.39% of Python3 online submissions for Palindrome Linked List.
"""
    
#partially working, O(N) time, but more than constant space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        stack = [head.val]
        head = head.next
        while head is not None:
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if head.val == temp:
                head = head.next
            else:
                stack.append(temp)
                stack.append(head.val)
                head = head.next
        
        return len(stack) == 0

"""
Fastest Solution (68ms):
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

#72ms solution doing what I tried to do better
class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        values = []
        
        while head:
            values.append(head.val)
            head = head.next
            
        return values == values[::-1]

Smallest Memory (22668 kb):
class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = self.reverse(slow.next)
        first = head
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    def reverse(self, cur):
        pre = None
        while cur:
            tmp = cur.next
"""
