# -*- coding: utf-8 -*-
from itertools import combinations, product

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        index_left_par = []  #记录左括号在的位置
        index_right_par = []  #记录右括号在的位置
        for i,e in enumerate(s):
            if e=='(':
                index_left_par.append(i)
            elif e==')':
                index_right_par.append(i)
        
        
        # 计算无效的(,)个数
        count = self.count_invalid_nums(s)
        
        # 移除对应 (, ) 数对应的所有可能
        all_possible = self.generate_all_possible(count, s, index_left_par, index_right_par)
    
        
        # 判断这个是否是有效的
        final_out = []
        for new_s in set( all_possible):
            if self.check_is_valid(new_s):
                final_out.append(new_s)
        return final_out
        
        
    def count_invalid_nums(self,s):
        '''计算 (, ) 无效个数'''
        stack  = []
        invalid_lst = []
        
        for e in s:
            if e=='(':
                stack.append(e)
            elif e==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    invalid_lst.append(e)
            else:
                pass
        
        invalid_lst += stack
        
        count = {'(':0,  ')':0}
        for e in invalid_lst:
            count[e] += 1
        return count
    
    def generate_all_possible(self, count, s, index_left_par, index_right_par) :
        left_remove = list(combinations(index_left_par, count['(']))
        right_remove = list(combinations(index_right_par, count[')']))
        all_possible = []
        for item in product(left_remove, right_remove):
            remove_index = set( item[0] ) | set(item[1])
            new_s = ''
            for i,e in enumerate(s):
                if i in remove_index:
                    pass
                else:
                    new_s+=e
            all_possible.append(new_s)
        return all_possible
    
    def check_is_valid(self, string):
        '''检查这个string是否包括的括号是否有效 True表示有效'''
        stack  = []
        
        for e in string:
            if e=='(':
                stack.append(e)
            elif e==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            else:
                pass
        return True

                
s =Solution()
print(s.removeInvalidParentheses("(a)())()" ))