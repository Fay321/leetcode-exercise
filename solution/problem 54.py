# -*- coding: utf-8 -*-
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = Counter()
        for e in p:
            p_count[e] += 1
        
        
        #初始化
        if len(s)<len(p):
            return []
        
        s_count = Counter()
        lst = []
        
        for e in s[:len(p)]:
            s_count[e] += 1
        
        if s_count == p_count:
            lst.append(0)
            
        #开始接下来计算
        l_p = len(p)
        for j in range(len(p),len(s)):
            value0 = s[j-l_p]
            if s_count[value0]==1:
                s_count.pop(value0)
            else:
                s_count[value0] -= 1
            s_count[s[j]] += 1
            
            if s_count==p_count:
                lst.append(j-l_p+1)
        return lst
    
s = Solution()
print(s.findAnagrams("cbaebabacd" , "abc"))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        