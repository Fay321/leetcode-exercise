# -*- coding: utf-8 -*-

class Solution_wrong(object):
    '''贪心法的思路无法解决这个问题'''
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()  #先从小到大排序
        num = 0
        for j in range(len(coins)-1,-1,-1):
            c = coins[j]
            num += amount//c
            print(c,amount//c, amount)
            
            amount -= (amount//c) * c
        if amount==0:
            return num
        else:
            return -1

class Solution(object):
    '''动态规划
    dp[i]表示兑换i元钱需要用的硬币数
    '''
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp =  dict()
        #初始化
        dp[0] = 0
        for i in range(1,amount+1):
            dp[i] = max(1e5,amount*3)   #用这个值代替inf值
        
        #递推式
        for i in range(1,amount+1):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        # 返回结果
        if dp[amount]==max(1e5,amount*3):
            return -1
        else:
            return dp[amount]
        
class Solution2:
    '''看见一个答案解法，其实也是用动态规划'''
    def coinChange(self, coins, amount):
        if amount < 1:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
                    
        if dp[amount] > amount:
            return -1
        
        return dp[amount]       
        
s = Solution()
print(s.coinChange([186,419,83,408],6249))