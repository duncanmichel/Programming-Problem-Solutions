"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = {}
        if head is None:
            return False
        visited[head] = True
        head = head.next
        while head is not None and head not in visited:
            visited[head] = True
            head = head.next
        return False if head is None else True

"""
My Solution:
Runtime: 44 ms, faster than 73.63% of Python online submissions for Linked List Cycle.
Memory Usage: 19 MB, less than 5.04% of Python online submissions for Linked List Cycle.
"""

"""
Fastest Solution (36ms):
class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        try:
            slow = head
            fast = head.next # should not be fast = head, otherwise will not enter while loop 
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

Smallest Memory (13992 kb):
class Solution(object):
    def hasCycle(self, head):
        while head:
            temp = head.next
            if temp == '0':
                return True
            head.next = '0'
            head = temp
        return False
"""
