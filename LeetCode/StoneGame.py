"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive 
integer number of stones piles[i].
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or 
the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
Example 1:
Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
Note:
2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

#Fastest!! (Matches fastest solution at 28ms runtime)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

"""
My Solution:
Runtime: 36 ms, faster than 84.81% of Python3 online submissions for Stone Game.
Memory Usage: 13.2 MB, less than 48.86% of Python3 online submissions for Stone Game.
"""

#Apparently this was wrong because it was short sighted (i.e. I needed to see not just which was the better move in terms of what
#Lee could take, but also in terms of what Alex's potential NEXT move was
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def bestMove():
            if len(piles) == 1:
                return 0
            elif len(piles) == 2:
                return 0 if piles[0]>piles[1] else 1
            first = max(piles[0]-piles[1],piles[0]-piles[-1])
            last = max(piles[-1]-piles[0],piles[-1]-piles[-2])
            return 0 if first >= last else -1
        
        alex = 0
        lee = 0
        size = len(piles)
        alexTurn = True
        while size > 0:
            stone = piles.pop(bestMove())
            if alexTurn:
                alex += stone
                alexTurn = False
                print("Alex took",stone,"to raise score to",alex,"; piles is now",piles)
            else:
                lee += stone
                alexTurn = True
                print("Lee took",stone,"to raise score to",lee,"; piles is now",piles)
            size -= 1
        return alex > lee

"""
Fastest Solution that actually calculates the answer (40ms)

class Solution:

    def stoneGame(self, piles) -> bool:
        can_win = False
        score = {False: 0, True: 0}
        i, j = 0, len(piles) - 1
        choice_stack = [(i, i, j, True), (j, i, j, True)]

        while not can_win and not choice_stack == []:
            choice, i, j, is_max_player = choice_stack.pop()

            score[is_max_player] += piles[choice]

            if i == j:
                if score[True] > score[False]:
                    return True

                score[is_max_player] -= piles[choice]

            max_i, max_j = i, j

            if choice == max_i:
                max_i += 1
            elif choice == max_j:
                max_j -= 1

            if max_i < j and max_i != choice:
                choice_stack.append((max_i, max_i, max_j, not is_max_player))
            if i < max_j and max_j != choice:
                choice_stack.append((max_j, max_i, max_j, not is_max_player))

        return can_win
        
#Approved Solution (DP)
from functools import lru_cache
class Solution:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0
"""
