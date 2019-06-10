# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        right_dic = {')':'(',']':'[','}':'{'}
        stack = []
        for p in s:
            if p not in right_dic:
                stack.append(p)
            else:
                if len(stack)>0 and stack.pop()==right_dic[p]:  #前面的条件是为了处理case "}"
                    pass
                else:
                    return False
        if len(stack)==0:  #注意stack为空，才说明都匹配完了
            return True
        else:
            return False