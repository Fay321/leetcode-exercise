# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/regular-expression-matching/
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s=='':
            if p=='':
                return True
            elif len(p)==1:
                return False
            else:
                if p[1]!='*':
                    return False
                else:
                    return self.isMatch(s,p[2:])
        
        if len(p)==0:
            if s!='':
                return False
            else:
                return True
        
        elif len(p)==1:
            if s=='' and p[0]!='':
                return False
            elif s[0]==p[0] or p[0]=='.':
                return self.isMatch(s[1:],p[1:])
            else:
                return False
        else:
            if s[0]==p[0] or p[0]=='.':
                if p[1]=='*':
                    return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])  #！！！！注意这里的or条件
                else:
                    return self.isMatch(s[1:],p[1:])
            else:
                if p[1]=='*':
                    return self.isMatch(s,p[2:])
                else:
                    return False