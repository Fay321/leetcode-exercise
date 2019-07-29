# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/task-scheduler/

先统计数组中各个任务出现的次数。优先安排次数最多的任务。
"""

from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter()
        for e in tasks:
            count[e] += 1
        
        max_times = max(count.values())
        remain_count = 0
        for e in count:
            if count[e]==max_times:
                remain_count += 1
        
        return max(len(tasks), (max_times-1)*(n+1)+remain_count )  #处理n=0的情况