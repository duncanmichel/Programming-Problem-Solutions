"""

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
My Solution:

"""

"""
Fastest Solution ():


Smallest Memory ():

"""
