# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        C = m+n -2
        c = m -1
        
        s = 1
        for i in range(C-c+1,C+1):
            s = s*i
            
        for j in range(1,c+1):
            s = s/j
        return s
    
s = Solution()
print(s.uniquePaths(3,2))