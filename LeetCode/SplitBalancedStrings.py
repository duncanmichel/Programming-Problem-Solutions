"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        lct = 0
        rct = 0
        #print ("String; ",s)
        for letter in s:
            if letter == 'R':
                if lct > 0:
                    lct -= 1
                elif rct == 0:
                    balance += 1
                    rct += 1
                else:
                    rct += 1
            else:
                if rct > 0:
                    rct -= 1
                elif lct == 0:
                    balance += 1
                    lct += 1
                else:
                    lct += 1
            #print("Letter: ",letter,", Balance: ",balance,", R count: ",rct,", L count: ",lct)
        return balance

"""
My Solution:
Runtime: 40 ms, faster than 43.83% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
"""

"""
Fastest Solution (24ms):
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        letter_counter = {"L": 0, "R": 0}
        splits = 0
        for letter in s:
            letter_counter[letter] += 1
            if letter_counter["L"] == letter_counter["R"] and letter_counter["L"] + letter_counter["R"] != 0:
                splits += 1
        return splits

Smallest Memory ():
NONE at this time
