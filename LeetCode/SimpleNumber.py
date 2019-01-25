"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        othernums = []
        for x in nums:
            if x in othernums:
                othernums.remove(x)
            else:
                othernums.append(x)
        for answer in othernums:
            return answer

"""
Fastest Solution:
    def singleNumber(self, nums):

        :type nums: List[int]
        :rtype: int

        
        return 2 * sum(set(nums)) - sum(nums)
        
Alternate:
    def singleNumber(self, nums):

        :type nums: List[int]
        :rtype: int


        Approach from SOLUTION:
        BIT MANIPULATION:
        Time complexity: O(N)
        Space complexity: O(1)
        If we take XOR of zero and some bit, it will return that bit
        a⊕0=a

        If we take XOR of two same bits, it will return 0
        a⊕a=0
        a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        

        a = 0
        for i in nums:
            a ^= i
        return a
"""

"""
Poor Solution (too long):
    def singleNumber(self, nums):

        :type nums: List[int]
        :rtype: int

        xct = 0
        yct = 0
        for x in nums:
            for y in nums:
                if xct == yct: #don't count same value
                    #print("[DEBUG] continuing over item "+str(xct)+" of value "+str(x))
                    yct += 1
                    continue
                if x == y: #found a duplicate
                    #print("[DEBUG] breaking from item "+str(yct)+" of value "+str(x)+" originally found at position "+str(xct))
                    yct += 1
                    break
                if yct == len(nums)-1: #made it to the end with no duplicates; found the ANS
                    return x
                yct += 1
            if xct == len(nums)-1: #last value of the list, with no other returned ANS
                return x
            xct += 1
            yct = 0
 """
