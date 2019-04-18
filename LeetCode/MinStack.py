"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.curMin = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.curMin:
            self.mins.append(self.curMin)
            self.curMin = x

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.curMin:
            self.curMin = self.mins.pop()

    def top(self) -> int:
        temp = self.stack.pop() #to do in constant time rather than iterate to last element
        self.stack.append(temp)
        return temp

    def getMin(self) -> int:
        return self.curMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
My Solution:
Runtime: 72 ms, faster than 39.89% of Python3 online submissions for Min Stack.
Memory Usage: 16.8 MB, less than 5.18% of Python3 online submissions for Min Stack.
"""

"""
Fastest Solution ():
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = float('inf')

    def push(self, x: 'int') -> 'None':
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> 'None':
        x = self.stack.pop()
        if x == self.min:
            self.min = self.stack.pop()

    def top(self) -> 'int':
        return self.stack[-1]

    def getMin(self) -> 'int':
        return self.min

Smallest Memory (15452 kb):
from collections import deque

class MinStack:

    def __init__(self):
        self.array = deque([])
        self.array_min = deque([])

    def push(self, x: 'int') -> 'None':
        self.array.append(x)
        if len(self.array_min) !=0:
            minimum = min(self.array_min[len(self.array_min)-1], x)
        else:
            minimum = x
        self.array_min.append(minimum)

    def pop(self) -> 'None':
        self.array.pop()
        self.array_min.pop()

    def top(self) -> 'int':
        return self.array[len(self.array)-1]

    def getMin(self) -> 'int':
        return self.array_min[len(self.array_min)-1]
"""
