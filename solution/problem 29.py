# -*- coding: utf-8 -*-
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count_dic = dict() #数字：次数
        for e in nums:
            if e in count_dic:
                count_dic[e] += 1
            else:
                count_dic[e] = 1
        
        
        lst = sorted(count_dic.items(),key=lambda item:item[1], reverse=True)[:k]
        lst = [e[0] for e in lst]
        return lst


s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))