# -*- coding: utf-8 -*-

class Solution1(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()  #长度：回文子串index[[start,end]]
        for l in range(1,len(s)+1):
            dic[l]  = []
            
            
        if len(s)<=1:
            return len(s)
        if len(s)==2:
            if s[0]==s[1]:
                return 3
            else:
                return 2
        
        final_count = 0
        #先记录一个字\两个字的回文
        for j in range(len(s)):
            dic[1].append([j,j+1])  #左闭右开
            final_count += 1
        
        for j in range(len(s)-1):
            if s[j]==s[j+1]:
                dic[2].append([j,j+2])  #左闭右开
                final_count += 1
        

        l = 3
        while l<=len(s):
            #长度为奇数的回文，左右加一个看是否还是回文
            for sub_s_index in dic[l-2]:
                i, j =sub_s_index
                if i>0 and j<len(s) and s[i-1] ==s[j]:
                    dic[l].append([i-1,j+1])
                    final_count+=1
            l += 1
        return final_count



'''前面自己思路是往左右看是否为回文，但是实现过程中有点繁琐，找到个下面更简单、快速的'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(2*n-1):
            left = i/2
            right = left + i%2
            while(left >= 0 and right < n and s[left]==s[right] ):
                res += 1
                left -= 1
                right += 1
        return res
    
    
s = Solution()
print(s.countSubstrings('abc'))
            
            
            
            
            
            
            
            
            
            
            