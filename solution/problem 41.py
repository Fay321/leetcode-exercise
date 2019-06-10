# -*- coding: utf-8 -*-
class Solution1(object):
    ''' 这个思路超时了'''
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_lst = [len(w) for w in wordDict]
        max_len = max(len_lst)
        min_len = min(len_lst)
        
        
        for i in range(max_len, min_len-1, -1):
            sub = s[0:i]
            if i>=len(s):
                if sub in wordDict:
                    return True
            else:
                if sub in wordDict:
                    sub_left_flag = self.wordBreak(s[i:], wordDict)
                    if sub_left_flag:
                        return True

'''使用记忆数组memo来保存所有已经计算过的结果，再下次遇到的时候，直接从cache中取，
而不是再次计算一遍。这种使用记忆数组memo的递归写法，和使用dp数组的迭代写法，
乃解题的两大神器，凡事能用dp解的题，一般也有用记忆数组的递归解法
'''

class Solution(object):
    ''' 这个思路超时了'''
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict)==0:  #边界条件
            return False
        
        op = dict()  #记录到位置i之前（不包括i）的字符串是否可以切成功，i最大值为len(s)
        max_len = max([len(w) for w in wordDict])
        
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                word = s[j:i]
                if len(word)> max_len:
                    break
                if j==0:  #说明需要判断是否在其中
                    if word in wordDict:
                        op[i] = True
                    else:
                        op[i] = False
                else:
                    if j in op and op[j]==True and word in wordDict:
                        op[i] = True
                        break
                    
        if len(s) in op:
            return op[len(s)]
        else:
            return False
                
                
                
                
    
    
    
    



s= Solution()
print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))