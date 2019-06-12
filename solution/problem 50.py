# -*- coding: utf-8 -*-

#-------------- 下面递归这个思路超时了 ------------------#
class Solution1(object):
    def generateParenthesis(self,n):
        tuple_lst = self.generateParenthesis_tuple(n)
        out_string_lst = []
        for tuple_one in tuple_lst:
            s = ''
            for e in tuple_one:
                if e==-1:
                    s+='('
                else:
                    s+=')'
            out_string_lst.append(s)
        return out_string_lst
    
    
    def generateParenthesis_tuple(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return {()}
        
        out_lst_set = set()
        
        for i in range(1,n*2):
            lst = [-1]+[0]*(n*2-1)  #第一个括号肯定是左括号
            lst[i] = 1
            
            for lst_part in self.generateParenthesis_tuple(n-1):
                lst = (lst[0],)+lst_part[:(i-1)]+(lst[i],)+lst_part[(i-1):]
                out_lst_set.add(lst)
        return out_lst_set


#---------------改思路 -------------------------#
''' 
这种有效的括号组合”()()(),(())()”的要求是假设这个长度是2n，那么在[1,2n][1,2n]区间里，任意一个位置，左括号’(‘肯定要大于等于右括号的个数不然就会“())”这种，是无效的括号组合。 
因此思路就是DFS，如果左括号的个数还有剩余，则+’(‘然后递归，如果右括号有剩余且小于左括号的个数则+‘）’。 
最后左右括号都不剩余的时候，也就是该排的都排完了，放入结果。

原文：https://blog.csdn.net/zl87758539/article/details/51643837 
代码：https://leetcode.com/problems/generate-parentheses/solution/
'''
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans = []
        def dfs(S='',left=0,right=0):
            if len(S)==2*n:
                print(S)
                ans.append(S)
                return 
            else:
                if left<n:
                    dfs(S+'(',left+1,right)
                    print('l',S+'(',left,right)
                if left>right:
                    dfs(S+')',left,right+1)
                    print('r',S+')',left,right)
        dfs()
        return ans

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        pass
        
        
        
        

s = Solution2()
print(s.generateParenthesis(3))