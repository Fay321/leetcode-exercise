# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        
        prices_diff = []
        for i in range(1,len(prices)):
            diff = prices[i]-prices[i-1]
            prices_diff.append(diff)
        
        s = 0
        max_s = 0
        for e in prices_diff:
            s = max(s+e, 0)
            if s>=max_s:
                max_s = s
        return max_s
    
    
s =Solution()
print(s.maxProfit([7,1,5,3,6,4]))