# -*- coding: utf-8 -*-
"""
Burst Balloons

两个难点没想到
1）dp的定义
2）递推式

我们维护一个二维动态数组 dp，其中 dp[i][j] 表示打爆区间 [i,j] 中的所有气球能得到的最多金币
k在区间 [i, j] 中，假如第k个气球最后被打爆，那么此时区间 [i, j] 被分成了三部分，[i, k-1]，[k]，和 [k+1, j]，只要我们之前更新过了 [i, k-1] 和 [k+1, j] 这两个子区间的 dp 值，可以直接用 dp[i][k-1] 和 dp[k+1][j]，那么最后被打爆的第k个气球的得分该怎么算呢，你可能会下意识的说，就乘以周围两个气球被 nums[k-1] * nums[k] * nums[k+1]，但其实这样是错误的，为啥呢？dp[i][k-1] 的意义是什么呢，是打爆区间 [i, k-1] 内所有的气球后的最大得分，此时第 k-1 个气球已经不能用了，同理，第 k+1 个气球也不能用了，相当于区间 [i, j] 中除了第k个气球，其他的已经爆了，那么周围的气球只能是第 i-1 个，和第 j+1 个了，所以得分应为 nums[i-1] * nums[k] * nums[j+1]
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:  #边界条件
            return 0
        
        dp = dict()  #{(i,j):max_value}   #含义：打爆位于[i,j]内【所有】气球的，能能到的最多金兵
        
        nums_dict = dict()
        nums_dict[-1] = 1
        nums_dict[len(nums)] = 1
        
        #初始值
        for i,v in enumerate(nums):
            nums_dict[i] = v
        
        #初始值注意
        for i, v in enumerate(nums):
            dp[(i,i)] = nums_dict[i]*nums_dict[i-1]*nums_dict[i+1]
        print(dp)
        
        for k in range(1,len(nums)):
            for i in range(len(nums)):
                
                if i+k>=len(nums):
                    break
                
                for j in range(i, i+k+1):  #[i,i+k]左闭右闭
                    #j_burst_value = nums_dict[j]*nums_dict[j-1]*nums_dict[j+1]  #这个式子有误
                    j_burst_value = nums_dict[j]*nums_dict[i-1]*nums_dict[i+k+1]  #注意！！！
                   
                    if j-1>=i: #从位置i到j气球左侧的打爆的最大值
                        j_burst_value += dp[(i,j-1)]
                    if j+1<=i+k:
                        j_burst_value += dp[(j+1,i+k)]
                    
                    
                    if (i,i+k) not in dp:
                        dp[(i,i+k)] = j_burst_value
                    else:
                        dp[(i,i+k)] = max(dp[(i,i+k)], j_burst_value)
        
            
        return dp[(0,len(nums)-1)]
