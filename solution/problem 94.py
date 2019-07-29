# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/evaluate-division/
ref:https://blog.csdn.net/fuxuemingzhu/article/details/82591165
"""
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = collections.defaultdict(dict)   ###注意这里
        for lst, value in zip(equations, values):
            a, b = lst
            dic[a][b] = value
            dic[b][a] =  1/value
        
        out_lst = []
        for q in queries:
            v = self.dfs(q[0],q[1],dic,{})
            out_lst.append(v)
        return out_lst
        
    def dfs(self, x, y, dic, visited):
        #为了防止在DFS中走已经走过了的路，所以需要使用visited保存每次已经访问过的节点。
        if x==y and x in dic:
            return 1
        
        visited.add(x)
        
        for z in dic[x]:    
            if z in visited:
                continue
            visited.add(z)
            d = self.dfs(z,y,dic,visited)
            if d!=-1:
                return dic[x][z]*d
        return -1
            
  