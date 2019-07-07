# -*- coding: utf-8 -*-
"""
思路参考:https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n =len(prices)
        buy = [0]* n#第i天持有股票时的最大收益
        sell = [0]*n #第i天没有持股的最大收益
        
        if len(prices)<=1:
            return 0
        
        for i in range(n):
            if i==0:
                sell[0] = 0
                buy[0] = -prices[0]
            else:
                sell[i] = max( sell[i-1], buy[i-1]+prices[i])
                buy[i] = max(buy[i-1], sell[i-2]-prices[i])
        
        return max(sell)

s = Solution()
print(s.maxProfit([1,2,3,0,2]))
