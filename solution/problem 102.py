# -*- coding: utf-8 -*-
"""
minimum-window-substring
"""

import re

class Solution1(object):
    ''' O(n*n)超时'''
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)<len(t):
            return ''
        
        dic = dict()  #记录从i位置到j位置（左闭右闭）替换掉这些字符后，T剩下的字符
        min_window_len = float('inf')
        min_window_s = ''
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j==i:
                    dic[(i,j)] = re.sub(s[j],'',t,count=1)
                else:
                    dic[(i,j)] = re.sub(s[j],'',dic[(i,j-1)],count=1)
                if dic[(i,j)]=='':
                    if j-i+1<min_window_len:
                        min_window_len  = j-i+1
                        min_window_s = s[i:(j+1)]
        return min_window_s
    
    
    
''' 
另外的思路：窗口右指针向右扩张用来找到包含子串为目的，窗口左指针向右收缩以使子串最小。
典型的滑动窗口方法的实现。

按照solution里的思路，自己写了如下代码
'''

from collections import Counter
import numpy as np

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = Counter()
        for e in t:
            count[e] += 1
        
        left_index = 0
        right_index = 0
        window_small_len = float('inf')
        window_small_s = ''
        
        while right_index<len(s):
            e = s[right_index]
            
            
            if e in count:
                count[e] -= 1
            
            #这时候left_index向右边划动
            while (np.array(list(count.values()))<=0).all():
                
                if right_index-left_index+1 < window_small_len:
                    window_small_len = right_index -  left_index + 1
                    window_small_s = s[left_index : (right_index+1)]
                    
                e = s[left_index]
                left_index += 1
                if e in count:
                    count[e] += 1
            right_index += 1
        return window_small_s
    
    
'''用示例的答案代码，速度更快'''

class Solution3(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        solution example
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)  #直接用这一行就可以对string中字符计数

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1  #也就是对出现在这个sub里的字符计数

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1   #formed也就是计算有多少个字符达到在t中个数的要求

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]