"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of 
their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse(node,before):
            if node is None:
                return before
            thisNode = ListNode(node.val)
            thisNode.next = before
            return reverse(node.next,thisNode)
        
        def adder(node1,node2,carry):
            if node1 is None and node2 is None:
                if carry:
                    return ListNode(carry)
                return None
            elif node1 is None:
                if carry:
                    val = node2.val + carry
                    node2.val = val % 10
                    node2.next = adder(node1,node2.next,val//10)
                return node2
            elif node2 is None:
                if carry:
                    val = node1.val + carry
                    node1.val = val % 10
                    node1.next = adder(node1.next,node2,val//10)
                return node1
            else:
                val = node1.val + node2.val + carry
                newNode = ListNode(val%10)
                newNode.next = adder(node1.next,node2.next,val//10)
                return newNode
            
        return reverse(adder(reverse(l1,None),reverse(l2,None),0),None)

"""
My Solution
Runtime: 104 ms, faster than 7.68% of Python online submissions for Add Two Numbers II.
Memory Usage: 12 MB, less than 7.53% of Python online submissions for Add Two Numbers II.
"""

"""
Fastest Solution (60ms):
class Solution(object):
    def addTwoNumbers(self, l1, l2):        
        def getNumber(l):
            curr = l
            string = 0
            while curr:
                string = string*10 + curr.val
                curr = curr.next
            return string
        
        def getLinkedList(number):
            if not number:
                return ListNode(0)
            res = None
            cur = res
            while number:
                val = number%10
                number = number//10
                pre = ListNode(val)
                pre.next = cur
                cur = pre
                
            return cur
        
        n = getNumber(l1)+getNumber(l2)
        return getLinkedList(n)
 

Smallest Memory (10676 kb):
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_stack, l2_stack = [], []
        
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
        
        max_length = max(len(l1_stack), len(l2_stack))
        if len(l1_stack) < max_length: l1_stack = [0]*(max_length-len(l1_stack)) + l1_stack
        if len(l2_stack) < max_length: l2_stack = [0]*(max_length-len(l2_stack)) + l2_stack
        
        nxt, rem = None, 0
        while l1_stack and l2_stack:
            res = l1_stack.pop() + l2_stack.pop() + rem
            res, rem = res%10, res//10
            curr = ListNode(res)
            curr.next = nxt
            nxt = curr        
            
        if rem:
            curr = ListNode(rem)
            curr.next = nxt
            return curr
        
        return nxt
"""
