"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary 
representation and return them as an array.
Example 1:
Input: 2
Output: [0,1,1]
Example 2:
Input: 5
Output: [0,1,1,2,1,2]
Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a 
single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

#Theory: if remainder of number divided by 2 is 1, add one. In either case, a number will have at least the same number of ones as the 
#number previous to it. My solution is O[N] runtime, where N is the integer we count up to, since it executes in one pass, with constant
#lookup of hash table, with O[N] extra space for the table.
class Solution:
    def countBits(self, num: int) -> List[int]:
        memo = {0:0,1:1,2:1}
        ans = []
        for number in range(num+1):
            ones = number%2 + memo[number//2]
            memo[number] = ones
            ans += [ones]
        return ans

"""
My Solution:
Runtime: 120 ms, faster than 50.67% of Python3 online submissions for Counting Bits.
Memory Usage: 18.8 MB, less than 5.22% of Python3 online submissions for Counting Bits.
"""

"""
Fastest Solution (88ms):
class Solution:
    def countBits(self, num):
        '''
        :type num: int
        :rtype: List[int]
        '''
        result = [0,1]
        temp = [1]
        while len(result) < num+2:
            temp = temp + [i+1 for i in temp]
            result += temp
        return result[:num+1]

Alt Fastest (92ms):
class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        if num % 2:
            result = [0]*(num+1)
        else:
            result = [0]*(num+2)
        result[1] = 1
        for i in range(1,num//2+1):
            result[i*2] = result[i]
            result[i*2+1] = result[i] + 1
        return result[:num+1]

Smallest Memory (14864 kb):
class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        out = [0, 1]
        start = 1
        
        while(len(out) <= num):
            
            for n in out[-start:]:
                out += [n, n+1]
                
            start *= 2
            
        return out[:num+1]
"""
