"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of 
the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

#still kind of long, but works for all cases

class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        profit = 0
        tempProfitA = 0
        tempProfitB =0
        branchProfit = 0
        
        if length == 0:
            return profit
        
        minBuy = prices[0]
        tempMin = minBuy
        for i in range(1,length):
            #print("profit",profit,"branchProfit",branchProfit,"minBuy",minBuy,"index",i,"current Price",prices[i])
            if branchProfit > 0 and prices[i] < prices[i-1]:
                tempProfitA = 0
                tempProfitB = branchProfit
                tempMin = prices[i]
                #print("testing a branch starting at index",i)
                for sub_index in range(i+1,length):
                    tempProfitA = max(tempProfitA,prices[sub_index]-tempMin)
                    tempProfitB = max(tempProfitB,prices[sub_index]-minBuy)
                if tempProfitB < tempProfitA + branchProfit:
                    profit += branchProfit
                    minBuy = tempMin
                    branchProfit = 0
            else:
                branchProfit = max(branchProfit,prices[i]-minBuy)
            minBuy = min(minBuy,prices[i])
        
        profit += branchProfit
        return profit

"""
#Functionally gets the right answer, but runs too long (recursive)
class Solution:
    
    def maxProfit_old(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0
        
        if length == 0:
            return profit
        
        minBuy = prices[0]
        for i in range(0,length):
            profit = max(profit,prices[i]-minBuy)
            minBuy = min(minBuy,prices[i])
                
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        profit = 0
        
        if length == 0:
            return profit
        
        minBuy = prices[0]
        for i in range(1,length):
            if profit > 0 and prices[i] < prices[i-1]:
                profit = max(profit,self.maxProfit_old(prices),prices[i-1]-minBuy + self.maxProfit(prices[i:]))
            else:
                profit = max(profit,prices[i]-minBuy)
            minBuy = min(minBuy,prices[i])
                
        return profit
"""

"""
My Solution
Runtime: 2884 ms, faster than 5.56% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""


"""
Fastest Solution (36ms):
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        last = prices[0]

        total = 0

        for price in prices:
            if price > last:
                total += price - last

            last = price

        return total


Smallest Memory (12604 kb):
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        total = 0
        for i in range(0, len(prices)-1) :
            if(prices[i+1]>prices[i]) :
                total += prices[i+1] - prices[i]
        return total
"""
