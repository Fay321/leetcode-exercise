# -*- coding: utf-8 -*-
# problem 2

# ver 1(88 ms	29.7 MB)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip()=='':  #边界情况
            return 0 if len(s)==0 else 1
        
        length_dict = dict()  #位置：[从这个位置到最后一位位置的最大substring长度，字串]
        for j in range(len(s)-1,-1,-1):
            if j==len(s)-1:
                length_dict[j] = [1,s[j]]
            else:
                if s[j] not in length_dict[j+1][1]:
                    length_dict[j] = [length_dict[j+1][0]+1,  s[j]+length_dict[j+1][1]]
                else:
                    length = 1 + length_dict[j+1][1].index(s[j])
                    string = s[j: (j+length)]
                    length_dict[j] = [length, string]
        return max([w[0] for w in length_dict.values()])
            
    
# ver2 (from discussion) 52 ms	11.2 MB
'''思路理解：
从左往右找，用start、res分别记最长字串的开始、长度；d是字典，{char:到目前这个char的最大index}
如果char未出现过，则 start不变、res会为 i-start+1
如果char出现过，则start要么是 这个char之前对应位置后移1位、要么是更后面的start，即max(start,d[ch]+1)
'''

class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in d: 
                start = max(start, d[ch]+1)
            res = max(res, i-start+1)                
            d[ch] = i
        return res