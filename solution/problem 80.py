'''
https://leetcode.com/problems/longest-palindromic-substring/
最长回文子串
'''
# -*- coding: utf-8 -*-
class Solution1(object):
    '''思路大致是中心扩散法 Spread From Center'''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        max_length = 0 #记录子串回文最大长度
        max_s = ''
        for i in range(len(s)):
            
            # 初始位置
            l=i-1
            r=i+1
            sub = s[i]
            
            #相同的扩展
            while l>=0:
                if s[l]==s[i]:
                    sub = s[l]+sub
                    l -= 1
                else:
                    break
            while r<len(s):
                if s[r]==s[i]:
                    sub = sub + s[r]
                    r += 1
                else:
                    break
                
            #往左右扩展
            while l>=0 and r<len(s):
                a = s[l]
                b = s[r]
                if a!=b:
                    break
                else:
                    sub = a+sub+b
                l -= 1
                r += 1
                    

            if len(sub)>max_length:
                max_s = sub
                max_length = len(sub)
        return max_s
    



'''有个经典的时间复杂度更低的算法：马拉车算法 Manacher Algorithm 
https://segmentfault.com/a/1190000002991199
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=='': #边界条件
            return ''
        
        new_s = '$#'  #需要补个位
        for e in s:
            new_s += e+'#'
        new_s += '^' #需要补个位
        
        mx = -1
        id = -1
        P = [0]*len(new_s)  #P记录把这个回文对折的长度 比如#a#长度为2
        
        max_d = 0
        max_len_sub_s = '' #记录最长回文子串
        
        for i,e in enumerate(new_s):
            if i<=1:
                P[i] = 1
                id = i
                mx = id+P[i]

            else:
                j = 2*id - i
                if P[j]+i<mx:
                    P[i] = P[j]
                else:
                    #P[i]>=mx
                    d = mx-i
                    while i+d<len(new_s):
                        if new_s[i+d]==new_s[i-d]:
                            d += 1
                        else:
                            break
                    
                    P[i] = d
                    
                    #更新mx
                    if i+P[i]>mx:
                        mx = i+d
                        id = i
                        
                if d>max_d:
                    max_d = d
                    max_len_sub_s = new_s[id-d+1:id+d]
        
        return max_len_sub_s.replace('#','')

s = Solution()
print(s.longestPalindrome('12212321'))
                                
        
        
        
        
        