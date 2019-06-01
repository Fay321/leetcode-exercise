# -*- coding: utf-8 -*-
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        dic = dict()
    
        for loc in range(len(intervals)):
            dic[loc] = intervals[loc]
    
        if len(intervals)<=1:
            return intervals
        
        i = 0
        while True:
            one_interval = dic[i]
            if i>=len(intervals)-1:
                break
            for j in range(i+1,len(intervals)):
                two_interval = dic[j]
                if self.check_two_interval_intersect(one_interval,two_interval):
                    combine_interval = [min(one_interval+two_interval),max(one_interval+two_interval)]
                    dic.pop(i)
                    dic[j] = combine_interval
                    break
            i+=1
        return list(dic.values())
    
    def check_two_interval_intersect(self, one, two):
        '''尝试改进1： 改进这个函数 '''
        if max(one[0],two[0])> min(one[1],two[1]):  #不相交的情况
            return False
        else:
            return True
        
        
        
s =Solution()
print(s.merge([[1,4],[0,2],[3,5]]))