# -*- coding: utf-8 -*-

'''用动态规划求解'''
class Solution1(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #candidate squares
        candidates_sqaures = []
        for j in range(1,n+1):
            if j*j <= n:
                candidates_sqaures.append(j*j)
            else:
                break
        
        #再类似于change coins思路，找到最小值
        dp =  dict()  # dp[i] 表示平方数之和为 i 的最小数目
        #初始化
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = n
        #递推式
        for i in range(1,n+1):
            for c in candidates_sqaures:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)
                else:
                    break
        return dp[n]


'''另一个思路：BFS
以12为例
list={1，4，9}
queue={12}
第一步分别用出列元素减list中的元素：queue={3,8,11}
第二步继续用上一步的三个方向继续向下遍历，可以得到第二步后的结果：queue={2,4,2,7,10}
第三步同上：queue={1,0,3,1,3,6,1,6,8}
这里出现了0，返回步数3
'''
from copy import deepcopy
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #candidate squares
        candidates_sqaures = []
        for j in range(1,n+1):
            if j*j <= n:
                candidates_sqaures.append(j*j)
            else:
                break
        
        #BFS
        layer_element = {n}
        new_layer_element = set()
        num = 0
        while 0 not in layer_element:
            for s in deepcopy(layer_element):
                for c in candidates_sqaures:
                    if s-c>=0:
                        new_layer_element.add(s-c)
            layer_element = new_layer_element
            num +=1
        return num
        
                





s =Solution()
print(s.numSquares(12))