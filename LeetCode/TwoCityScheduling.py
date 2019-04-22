"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of 
flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Note:
1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2
        costs.sort(key = lambda item:item[0]-item[1])
        return sum(costs[i][0] for i in range(N)) + sum(costs[i][1] for i in range(N,2*N))
        '''
        alist = []
        blist = []
        for person in costs:
            if person[0]-person[1] < 0:
                alist.append(person)
            else:
                blist.append(person)
        print(alist)
        print(blist)
        alist.sort(key=lambda item:item[0]-item[1])
        blist.sort(key=lambda item:item[1]-item[0])
        
        while len(alist) < N:
            alist.append(blist.pop())
        while len(blist) < N:
            blist.append(alist.pop())
        print(alist)
        print(blist)
            
        return sum(alist[i][0] for i in range(N)) + sum(blist[i][1] for i in range(N)) 
        '''

"""
My Solution: 
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Two City Scheduling.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Two City Scheduling.
"""

"""
Fastest Solution:
[As of submission, mine was!]

Smallest Memory:
[As of submission, not enough data]
