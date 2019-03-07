"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to 
find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = (len(prices))
        pArr = [0]*(length)
        if prices == []:
            return 0
        for i in range(0,length-1):
            sellVal = max(prices[i+1:])
            pArr[i] = max(0,sellVal-prices[i])
                
        return max(pArr)

"""
My Solution
Runtime: 5920 ms, faster than 5.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.2 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

"""
Approved Solution (one pass, in JAVA)
public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}

PYTHON Version (40ms):
class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        
        lowp = prices[0]
        maxp = 0
        for p in prices[1:]:
            if p < lowp:
                lowp = p
            elif p - lowp > maxp:
                maxp = p - lowp
                
        return maxp
"""

"""
Fastest Solution (36ms)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_p = prices[0]
        ma_p = 0
        for price in prices:
            if price < min_p:
                min_p = price
            if price - min_p > ma_p:
                ma_p = price - min_p
        return ma_p
"""
