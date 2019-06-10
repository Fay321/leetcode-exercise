# -*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'1':[''],
               '2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        if len(digits)==0:  #边界条件
            return ''
        res_lst = []
        for s in dic[digits[0]]:
            if len(digits)==1:
                res_lst.append(s)
            else:
                res_lst += [ s+string for string in self.letterCombinations(digits[1:])]
        return res_lst
    
    
s = Solution()
print(s.letterCombinations('2'))
            