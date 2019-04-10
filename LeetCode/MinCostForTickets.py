"""
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will 
travel is given as an array days.  Each day is an integer from 1 to 365.
Train tickets are sold in 3 different ways:
a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 
day 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
Note:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        [ONE_DAY_PASS,SEVEN_DAY_PASS,THIRTY_DAY_PASS],travel_days = costs,days
        best_cost_to_here = {day:float('inf') for day in range(366)}
        isTravelDay = {day:False for day in range(366)}
        total = 0
        size = len(days)
        
        if size == 1:
            return ONE_DAY_PASS
        
        #initialize first days and costs
        firstDay = travel_days[0]
        best_cost_to_here[firstDay] = ONE_DAY_PASS
        for day in range(0,firstDay):
            best_cost_to_here[day] = 0
        
        for day in travel_days:
            isTravelDay[day] = True
        for day in range(firstDay+1,travel_days[size-1]+1):
            if not isTravelDay[day]:
                best_cost_to_here[day] = best_cost_to_here[day-1]
                continue
            for prev_day in range(max(day-30,firstDay-1,0),day):
                best_cost_to_here[day] = min(best_cost_to_here[day],best_cost_to_here[prev_day]+THIRTY_DAY_PASS)
                if prev_day + 7 >= day:
                    best_cost_to_here[day] = min(best_cost_to_here[day],best_cost_to_here[prev_day]+SEVEN_DAY_PASS)
                    if prev_day + 1 >= day:
                        best_cost_to_here[day] = min(best_cost_to_here[day],best_cost_to_here[prev_day]+ONE_DAY_PASS)
        print(best_cost_to_here)

        return best_cost_to_here[travel_days[size-1]]

"""
My Solution:
Runtime: 84 ms, faster than 10.20% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 13.2 MB, less than 14.89% of Python3 online submissions for Minimum Cost For Tickets.
"""

"""
Fastest Solution (36ms):
class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        seven_days_queue = []
        thirty_days_queue = []
        total = 0
        for day in days:
            while len(seven_days_queue) and seven_days_queue[0][0] + 7 <= day: seven_days_queue.pop(0)
            while len(thirty_days_queue) and thirty_days_queue[0][0] + 30 <= day: thirty_days_queue.pop(0)
            seven_days_queue.append((day, total+costs[1]))
            thirty_days_queue.append((day, total+costs[2]))
            total = min(total+costs[0], seven_days_queue[0][1], thirty_days_queue[0][1])
        return total

Smallest Memory (12272 kb):
class Solution:    
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':    
        if len(days) == 0:
            return 0
        
        c1, c7, c30 = costs  # for easier understanding
        min_cost = min(costs)
        memo = [0] * (len(days) + 1)
        
        for i in range(len(days)-1, -1, -1): # go through days
            memo[i] = memo[i+1] + min_cost  # take the lowest priced ticket
            # Nothing to do anymore for day pass
     
            # for 7 day pass
            for j in range(i+1, len(days)):
                if days[i] + 7 > days[j]: # days[j] is out of window for 7 days pass
                    memo[i] = min(memo[i], c7 + memo[j+1])

                # for 30 days pass
                if days[i] + 30 <= days[j]:
                    break
                memo[i] = min(memo[i], c30 + memo[j+1])

        return memo[0]
"""
