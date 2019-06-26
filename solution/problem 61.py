# -*- coding: utf-8 -*-
''' 拓扑排序加速
https://wulc.me/2016/07/27/LeetCode%20%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A(207,210)--%E6%8B%93%E6%89%91%E6%8E%92%E5%BA%8F/
'''

import numpy as np

class Solution1(object):
    ''' 【思路：判断有向图中是否有环 (解决方法：拓扑排序）】
    最直观的方法步骤如下
    （1） 找到图中入度（indegree）为0的点，然后记录这个点并删除这个点的所有出度（outdegree），也就是连接了这个点的其他点的入度
    （2） 检查图中是否有入度为0的点，如果有重复步骤（1）
    '''
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        array  = np.zeros((numCourses, numCourses))
        
        
        for prep in prerequisites:
            array[prep[0], prep[1]] = 1
        
        
        
        #去掉入度为0的
        while True:
            #print(array, array.sum(0).shape, type(array.sum(0)))
            print(array, array.sum(0))
            #计算入度
            if len(array.shape)<=1 or array.shape[0]<=1:  #如果array为空了，或者只有一个点在其中了
                return True
            elif array.sum(0).shape==() and array.sum(0) != 0:  
                return False
            elif array.sum(0).shape!=() and 0 not in array.sum(0):
                return False
            
            #去掉入度为0的 [即保留入度非0的]
            #print(array, array.sum(0), array.shape)
            array = array[:,array.sum(0)!=0][array.sum(0)!=0]
        
class Solution(object):
    ''' 这个代码速度更快'''
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for i in range(numCourses)] 
        
        connection = {i:[] for i in range(numCourses)}
        for link in prerequisites:
            connection[link[1]].append(link[0])
            indegree[link[0]] += 1
            
        zero_indegree = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        
        ############## 主要这里的循环思路更快些 ###############
        i = 0
        while i<len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if  indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        ##################################################
        
        
        if len(zero_indegree) == numCourses:
            return True
        else:
            return False   

  
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        #拓扑排序思路：挨着去掉0入度的点，如果最后0入度的点个数等于numCourses，则返回True
        to_df = np.array([0]*numCourses)
        id_array = np.array(range(numCourses))
        linked = dict()  #记录  from:[to1,to2]
        for j in id_array:
            linked[j] = []
        for prep in prerequisites:
            
            from_id, to_id = prep
            to_df[to_id] += 1
            linked[from_id].append(to_id)
        
        remove_zero_ids = set()
        while True:
            zero_ids = set( id_array[to_df==0]) - set(remove_zero_ids)
            remove_zero_ids = remove_zero_ids | zero_ids
            
            if len(zero_ids)==0:  #停止条件
                break
            
            for zero_id in zero_ids:
                for to_id in linked[zero_id]:
                    to_df[to_id] -= 1
            
        
        if len(remove_zero_ids)==numCourses:
            return True
        else:
            return False
        
        
        
        
        
        
        
s = Solution()
print(s.canFinish(2, [[0, 1]]))
            
            